from django.contrib import admin

from .models import CartModel,CartItemModel

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display  = [
        'user',
    ]
@admin.register(CartItemModel)
class CartItemAdmin(admin.ModelAdmin):
    list_display  = [
        'cart',
        'product',
        'quantity',
    ]