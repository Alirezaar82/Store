from django.contrib import admin

from .models import *

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(CouponModel)
class CouponAdmin(admin.ModelAdmin):
    pass
