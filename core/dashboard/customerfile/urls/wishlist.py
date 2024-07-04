from django.urls import path
from .. import views



urlpatterns = [
    path('wishlist-list/',views.CustomerWishlistView.as_view(),name='wishlist-list'),
    path('wishlist/<int:pk>/delete/',views.CustomerWishlistDeleteView.as_view(),name='wishlist-delete'),
]

