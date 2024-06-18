from django.urls import path
from .. import views



urlpatterns = [
    path('coupon-list/',views.AdminCouponListView.as_view(),name='coupon-list'),
    path('coupon/<slug>/detail/',views.AdminCouponDetailView.as_view(),name='coupon-detail'),
    path('coupon/<int:pk>/edit/',views.AdminCouponEditView.as_view(),name='coupon-edit'),
    path('coupon/<int:pk>/delete/',views.AdminCouponDeleteview.as_view(),name='coupon-delete'),
    path('coupon/create/',views.AdminCouponCreateView.as_view(),name='coupon-create'),
]


