from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.views.generic import FormView,TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count

from accounts.models import UserAddressModel
from .forms import OrderCheckOutForm
from .models import CouponModel,OrderModel,OrderItemModel
from cart.models import CartModel,CartItemModel
from payment.zarinpall_client import ZarinPalSandBox
from payment.models import Paymentmodel


class OrderCheckOutView(LoginRequiredMixin,FormView):
    template_name = 'order/checkout.html'
    form_class = OrderCheckOutForm
    success_url = reverse_lazy('order:completed')

    def get_form_kwargs(self):
        kwargs = super(OrderCheckOutView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        user = self.request.user
        cleaned_data = form.cleaned_data
        address = cleaned_data['address_id']
        coupon = cleaned_data['coupon']

        cart = CartModel.objects.prefetch_related('cart_items').get(user=user)
        order = self.create_order(address,user)

        self.create_order_item(order,cart)
        total_price = order.calculate_total_price()
        self.apply_coupon(coupon,order,user,total_price)
        order.save()
        return redirect(self.create_payment_url(order))
    
    def create_payment_url(self,order):
        zarinpal = ZarinPalSandBox()
        response = zarinpal.payment_request(
            amount=order.get_price()
        )
        payment_obj = Paymentmodel.objects.create(
            authority_id = response.get('Authority'),
            amount = order.get_price()
        )
        order.payment = payment_obj
        order.save()
        return zarinpal.generate_payment_url(response.get("Authority"))

    def form_invalid(self, form):
        
        return super().form_invalid(form)

    
    def create_order(self,address,user):
        return OrderModel.objects.create(
            user = user,
            address = address.address,
            state = address.state,
            city = address.city,
            zip_code = address.zip_code,
        )

    def create_order_item(self,order,cart):
        for item in cart.cart_items.all():
            OrderItemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                single_price=item.product.get_price(),
                total_price=item.get_price(),
            )

    def apply_coupon(self, coupon, order, user, total_price):
        if coupon:

            order.coupon = coupon
            coupon.used_by.add(user)
            coupon.save()

        order.total_price = total_price
        order.discount_price = order.get_price()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartModel.objects.get(user=self.request.user)
        context["addresses"] = UserAddressModel.objects.filter(
            user=self.request.user)
        total_price = cart.calculate_total_price()
        context["total_price"] = total_price
        context["total_tax"] = round((total_price * 9)/100)
        return context
    
class ValidateCouponView(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        code = request.POST.get("code")
        user = self.request.user

        status_code = 200
        message = "کد تخفیف با موفقیت ثبت شد"
        total_price = 0
        total_tax = 0

        try:
            coupon = CouponModel.objects.get(code=code)
        except CouponModel.DoesNotExist:
            return JsonResponse({"message": "کد تخفیف یافت نشد"}, status=404)
        else:
            if coupon.used_by.count() >= coupon.max_limit_usage:
                status_code, message = 403, "محدودیت در تعداد استفاده"

            elif coupon.expiration_date and coupon.expiration_date < timezone.now():
                status_code, message = 403, "کد تخفیف منقضی شده است"

            elif user in coupon.used_by.all():
                status_code, message = 403, "این کد تخفیف قبلا توسط شما استفاده شده است"
            else:
                cart = CartModel.objects.get(user=self.request.user)

                total_price = cart.calculate_total_price()
                total_price = round(
                    total_price - (total_price * (coupon.discount_percent/100)))
                total_tax = round((total_price * 9)/100)
        return JsonResponse({"message": message, "total_tax": total_tax, "total_price": total_price}, status=status_code)
    
class OrderCompletedView(LoginRequiredMixin,TemplateView):
    template_name = "order/completed.html"
    
class OrderFailedView(LoginRequiredMixin,TemplateView):
    template_name = "order/failed.html"

