from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import View

from .models import Paymentmodel,PaymentStatusType
from .zarinpall_client import ZarinPalSandBox
from order.models import OrderModel,OrderStatusType
from cart.cart import CartMain
from cart.models import CartModel


class PaymentVerifyView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        authority_id = request.GET.get('Authority')
        status = request.GET.get('Status')

        payment_obj = get_object_or_404(
            Paymentmodel,authority_id=authority_id
        )
        cart = CartModel.objects.get(user=user)
        order = OrderModel.objects.get(payment=payment_obj)
        zarinpal = ZarinPalSandBox()

        response = zarinpal.payment_verify(
           int(payment_obj.amount), payment_obj.authority_id)
        
        Ref_id = response['RefID']
        status_code = response['Status']

        payment_obj.ref_id = Ref_id
        payment_obj.response_code = status_code
        payment_obj.response_json = response

        if status_code in {100,101}:
            payment_obj.status = PaymentStatusType.success.value
            payment_obj.save()
            order.status = OrderStatusType.success.value
            order.save()
            self.clear_cart(cart)
        else:
            payment_obj.status = PaymentStatusType.failed.value
            payment_obj.save()
            order.status = OrderStatusType.failed.value
            order.save()

        return redirect(reverse_lazy("order:completed") if status_code in {100, 101} else reverse_lazy("order:failed"))



    def clear_cart(self, cart):
        cart.cart_items.all().delete()
        CartMain(self.request).clear()
