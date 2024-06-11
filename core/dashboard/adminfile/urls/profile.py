from django.urls import path
from .. import views



urlpatterns = [
    path('profile-edit/',views.AminProfileUpdateView.as_view(),name='profile-edit'),
    path('image-edit/',views.AdminProfileImageUpdateView.as_view(),name='image-edit'),
]


