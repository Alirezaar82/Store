from django.urls import path
from .. import views



urlpatterns = [
    path('profile-edit/',views.CustomerProfileUpdateView.as_view(),name='profile-edit'),
    path('image-edit/',views.customerProfileImageUpdateView.as_view(),name='image-edit'),
]


