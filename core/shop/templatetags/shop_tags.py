from django import template

from shop.models import ProductModel,ProductStatusType,WishlistProductModel

register = template.Library()

@register.inclusion_tag('includes/latest-products.html',takes_context=True)
def show_latest_products(context):
    request = context.get("request")
    latest_products = ProductModel.objects.prefetch_related('category').filter(
        status=ProductStatusType.publish.value,stock__gte=1).distinct().order_by("-datetime_created")[:8]
    # wishlist_items = WishlistProductModel.objects.filter(user=request.user).values_list("product__id",flat=True) if request.user.is_authenticated else []
    return {"latest_products": latest_products,"request":request,}
    
@register.inclusion_tag('includes/similar-products.html',takes_context=True)
def show_similar_products(context,product):
    request = context.get("request")
    product_categories= product.category.all()
    similar_products = ProductModel.objects.prefetch_related('category').filter(
        status=ProductStatusType.publish.value,category__in=product_categories,stock__gte=1).distinct().exclude(id=product.id).order_by("-datetime_created")[:4]
    # wishlist_items = WishlistProductModel.objects.filter(user=request.user).values_list("product__id",flat=True) if request.user.is_authenticated else []
    return {"similar_products": similar_products,"request":request}
    