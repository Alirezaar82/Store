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
    

class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE)
    product = models.ForeignKey('shop.ProductModel',on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-datetime_created"]

    def __str__(self):
        return f'{self.cart}'
