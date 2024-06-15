from django.urls import path
from .. import views



urlpatterns = [
    path('logo/<int:pk>/edit/',views.AdminLogoEditView.as_view(),name='logo-edit'),
]


