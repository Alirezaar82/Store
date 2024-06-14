from django.urls import path
from .. import views



urlpatterns = [
    path('products-list/',views.AdminProductsListView.as_view(),name='products-list'),
    path('product/<slug>/detail/',views.AdminProductDetailView.as_view(),name='product-detail'),
    path('product/<int:pk>/edit/',views.AdminProductEditView.as_view(),name='product-edit'),
    path('product/<int:pk>/delete/',views.AdminProductDeleteview.as_view(),name='product-delete'),
    path('product/create/',views.AdminProductCreateView.as_view(),name='product-create'),
]


