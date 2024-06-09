from django.urls import path

from . import views


app_name = 'order'

urlpatterns = [
    path('check-out/',views.OrderCheckOutView.as_view(),name='check-out'),
    path('validate-coupon/',views.ValidateCouponView.as_view(),name='validate-coupon'),
    path('complete/',views.OrderCompletedView.as_view(),name='complete'),
    path('failed/',views.OrderFailedView.as_view(),name='failed'),
]