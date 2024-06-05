from typing import Any
from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,FormView
from django.http import JsonResponse


from .cart import CartMain
from shop.models import ProductModel,ProductStatusType

class AddOneToCartView(View):
    def post(self, request, *args, **kwargs):
        cart = CartMain(request)
        product_id = request.POST.get('product_id')
        
        if product_id and ProductModel.objects.filter(status=ProductStatusType.publish.value,stock__gte=1):
            message = cart.addonecart(product_id)

        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity(),'message':message,})
        
class RemoveCartView(View):

    def post(self, request, *args, **kwargs):
        cart = CartMain(request)
        product_id = request.POST.get('product_id')

        if product_id:
            message = cart.remove_product(product_id)

        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity(),'message':message,})

class UpdateProductQuantityView(View):
    def post(self,request,*args,**kwargs):
        cart = CartMain(request)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        if product_id and ProductModel.objects.filter(status=ProductStatusType.publish.value,stock__gte=1):
            message = cart.update_product_quantity(product_id,quantity)

        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity(),'message':message,})
        
        
class CartSummaryView(TemplateView):
    template_name = 'cart/cartsummary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartMain(self.request)
        cart_item = cart.get_cart()
        context["cart_item"] = cart_item
        context["total_quantity"] = cart.get_total_quantity()
        context["total_payment_price"] = cart.get_total_payment_amount()
        return context
    
class AddCartView(View):

    def post(self, request, *args, **kwargs):
        cart = CartMain(request)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if product_id and ProductModel.objects.filter(status=ProductStatusType.publish.value,stock__gte=1):
            message = cart.addcart(product_id,quantity)
            product = ProductModel.objects.get(id=product_id)

        return redirect(reverse_lazy('shop:product-detail',kwargs={"slug":product.slug}))
