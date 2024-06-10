from django.urls import path

from .views import PaymentVerifyView
urlpatterns = [
    path('verify',PaymentVerifyView.as_view(),name='verify')
 
]