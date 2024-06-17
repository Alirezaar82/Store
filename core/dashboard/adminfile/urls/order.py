from django.urls import path
from .. import views



urlpatterns = [
    path('order-list/',views.AdminOrdersListView.as_view(),name='order-list'),
    path('order/<int:pk>/detail/',views.AdminOrderEditView.as_view(),name='order-detail'),
    # path('order/<int:pk>/edit/',views.AdminOrderEditView.as_view(),name='order-edit'),
    path('order/<int:pk>/invoice/',views.AdminOrderInvoiceView.as_view(),name='order-invoice'),

]
