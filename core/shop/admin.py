from django.contrib import admin

from .models import ProductModel,ProductCategoryModel,ProductImages,WishlistProductModel,ReviewModel

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
        'list_products',  # Add the method to list display
    ]
    
    def list_products(self, obj):
        # Fetch related products
        products = ProductModel.objects.filter(category=obj).count()
        # Create a string of product titles
        return products
    
    # Set the method's short description for the admin interface

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    pass
@admin.register(WishlistProductModel)
class WishlistProductAdmin(admin.ModelAdmin):
    pass
@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    pass