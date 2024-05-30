from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
  path('products/grid/',views.ProductsGridView.as_view(),name='products-grid'),
  path('product/<slug>/detail/',views.ProductDetailView.as_view(),name='product-detail'),
] 