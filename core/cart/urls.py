from django.urls import path

from . import views


app_name = 'cart'

urlpatterns = [
    path('add-product/',views.AddCartView.as_view(),name='add-cart-product'),
    path('add-one-product/',views.AddOneToCartView.as_view(),name='add-one-to-cart'),
    path('remove/',views.RemoveCartView.as_view(),name='remove-product'),
    path('update/',views.UpdateProductQuantityView.as_view(),name='update-product-quantity'),
    path('summary/',views.CartSummaryView.as_view(),name='cart-summary'),
]