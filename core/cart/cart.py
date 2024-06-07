from django.contrib import messages
from django.shortcuts import get_object_or_404

from shop.models import ProductStatusType,ProductModel
from .models import *

class CartMain:

    def __init__(self, request):
        self.request = request
        self.session = self.request.session
        self._cart = self.session.setdefault("cart", {"items": []})

    def update_product_quantity(self,product_id,quantity):
        message = ''
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                item["quantity"] = int(quantity)
                message = 'ایتم با موفقیت آپدیت شد'
                break
        else:
            return
        self.save()
        return message
    
    def remove_product(self,product_id):
        for item in self._cart["items"]:
            if product_id == item["product_id"]:
                self._cart["items"].remove(item)
                message = 'ایتم با موفقیت حذف شد'
                break
        else:
            return
        self.save()
        return message
    
    def addonecart(self, product_id):
        product = get_object_or_404(ProductModel,id=product_id)
        message = ''
        for item in self._cart["items"]:
                if product_id == item["product_id"]:
                    if item['quantity'] <  product.stock:
                        item["quantity"] += 1
                        message = 'ایتم به سبد خرید شما اضافه شد'
                    else:
                        message = 'موجودی محصول کافی نمی باشد'
                    break
        else:
            new_item = {"product_id": product_id, "quantity": 1}
            self._cart["items"].append(new_item)
            message = 'ایتم به سبد خرید شما اضافه شد'
        self.save()
        return message
    
    def addcart(self, product_id,quantity):
        this_quantity = int(quantity)
        product = get_object_or_404(ProductModel,id=product_id)
        message = ''
        if this_quantity == 0 :
            return messages.warning(self.request,'تعداد نمیتواند برابر صفر باشد')
         
        if this_quantity >  product.stock:
            return messages.warning(self.request,'موجودی محصول کافی نمی باشد')

        for item in self._cart["items"]:
                if product_id == item["product_id"]:
                    if item['quantity'] <  product.stock:
                        item["quantity"] += this_quantity
                        messages.success(self.request,f'ایتم به تعداد {this_quantity} سبد خرید شما اضافه شد')
                    else:
                        messages.warning(self.request,'موجودی محصول کافی نمی باشد')
                    break
        else:
            new_item = {"product_id": product_id, "quantity": this_quantity}
            self._cart["items"].append(new_item)
            messages.success(self.request,f'ایتم به تعداد {this_quantity} سبد خرید شما اضافه شد')
        self.save()
        

    def clear(self):
        self._cart = self.session["cart"] = {"items": []}
        self.save()

    def get_cart_dict(self):
        return self._cart

    def get_cart(self):
        for item in self._cart["items"]:
            product_obj = ProductModel.objects.get(id=item["product_id"], status=ProductStatusType.publish.value)
            item.update({"product_obj": product_obj, "total_price": item["quantity"] * product_obj.get_price()})

        return self._cart["items"]

    def get_total_payment_amount(self):
        return sum(item["total_price"] for item in self._cart["items"])

    def get_total_quantity(self):
        return sum(item["quantity"] for item in self._cart["items"])

    def save(self):
        self.session.modified = True


    # def sync_cart_items_from_db(self,user):
    #     cart,created = CartModel.objects.get_or_create(user=user)
    #     cart_items = CartItemModel.objects.filter(cart=cart)
        
    #     for cart_item in cart_items:
    #         for item in self._cart["items"]:
    #             if str(cart_item.product.id) == item["product_id"]:
    #                 cart_item.quantity = int(item["quantity"])
    #                 print('**********************************************************************')
    #                 print('in merge')
    #                 print(item["quantity"])
    #                 print('**********************************************************************')
    #                 cart_item.save()
    #                 break
    #         else:
    #             new_item = {"product_id": str(cart_item.product.id), "quantity": cart_item.quantity}
    #             self._cart["items"].append(new_item)

    #     self.merge_session_cart_in_db(user)
    #     self.save()
            
        
    # def merge_session_cart_in_db(self,user):
    #     cart,created = CartModel.objects.get_or_create(user=user)
        
    #     for item in  self._cart["items"]:
    #         product_obj = ProductModel.objects.get(id=item["product_id"], status=ProductStatusType.publish.value)
            
    #         cart_item ,created = CartItemModel.objects.get_or_create(cart=cart,product=product_obj)
    #         cart_item.quantity = int(item["quantity"])
    #         print('**********************************************************************')
    #         print('in merge')
    #         print(item["quantity"])
    #         print('**********************************************************************')

    #         cart_item.save()

    #     session_product_ids = [item["product_id"] for item in  self._cart["items"]]
    #     CartItemModel.objects.filter(cart=cart).exclude(product__id__in=session_product_ids).delete()

    def sync_cart_items_from_db(self,user):
    
        cart,created = CartModel.objects.get_or_create(user=user)
        cart_items = CartItemModel.objects.filter(cart=cart)
        
        for cart_item in cart_items:
            for item in self._cart["items"]:
                if str(cart_item.product.id) == item["product_id"]:
                    cart_item.quantity = item["quantity"]
                    cart_item.save()
                    break
            else:
                new_item = {"product_id": str(cart_item.product.id), "quantity": cart_item.quantity}
                self._cart["items"].append(new_item)
        self.merge_session_cart_in_db(user)
        self.save()
            
        
    def merge_session_cart_in_db(self,user):
        cart,created = CartModel.objects.get_or_create(user=user)
        
        for item in  self._cart["items"]:
            
            product_obj = ProductModel.objects.get(id=item["product_id"], status=ProductStatusType.publish.value)
            
            cart_item ,created = CartItemModel.objects.get_or_create(cart=cart,product=product_obj)
            cart_item.quantity = item["quantity"]
            cart_item.save()
        session_product_ids = [item["product_id"] for item in  self._cart["items"]]
        CartItemModel.objects.filter(cart=cart).exclude(product__id__in=session_product_ids).delete()
        