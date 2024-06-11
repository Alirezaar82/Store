from django.urls import path
from .. import views



urlpatterns = [
    path('home/',views.AdminHomeView.as_view(),name='home')
]


