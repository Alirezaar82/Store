from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class CartModel(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.user}'
    
    def calculate_total_price(self):
        return sum(item.product.get_price() * item.quantity for item in self.cart_items.all())
    
    

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE,related_name="cart_items")
    product = models.ForeignKey('shop.ProductModel',on_delete=models.CASCADE)

    
    quantity = models.PositiveIntegerField(default=0)


    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.cart}'
    
    def get_price(self):
        return self.quantity * self.product.get_price()
        
