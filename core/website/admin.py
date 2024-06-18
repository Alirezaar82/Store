from django.contrib import admin

from .models import *


@admin.register(LogoModel)
class LogoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]
    
@admin.register(ContactUsModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
    ]
