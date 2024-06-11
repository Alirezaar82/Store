from django.urls import path
from .. import views



urlpatterns = [
    path('home/',views.CustomerHomeView.as_view(),name='home')
]


