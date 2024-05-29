from django.contrib import admin

from .models import ProductModel,ProductCategoryModel,ProductImages

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'slug',
        'get_categories',
        'price',
        'status',
        'stock',
        'discount_percent',
    ]
@admin.register(ProductCategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'slug',
    ]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass