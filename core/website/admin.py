from django.contrib import admin

from .models import *


@admin.register(LogoModel)
class LogoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
    ]