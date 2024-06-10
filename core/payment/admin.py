from django.contrib import admin

from .models import Paymentmodel

@admin.register(Paymentmodel)
class PaymentAdmin(admin.ModelAdmin):
    pass