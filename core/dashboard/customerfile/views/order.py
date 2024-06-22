from django.views.generic import ListView,DetailView
from django.core.exceptions import FieldError
from django.contrib.auth.mixins import LoginRequiredMixin

from order.models import *
from dashboard.permissions import HasCustomerAccessPermission

class CustomerOrdersListView(LoginRequiredMixin,HasCustomerAccessPermission,ListView):
    template_name = 'dashboard/customer/orders/order-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = OrderModel.objects.prefetch_related('order_items').filter(user=self.request.user)
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(id__icontains=search_q)
        if status := self.request.GET.get("status"):
            queryset = queryset.filter(status=status)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()  
        context["status_types"] = OrderStatusType.choices
        return context
    
class CustomerOrderDetailView(LoginRequiredMixin, HasCustomerAccessPermission, DetailView):
    template_name = "dashboard/customer/orders/order-detail.html"

    def get_queryset(self):
        return OrderModel.objects.prefetch_related('order_items').filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    
class CustomerOrderInvoiceView(LoginRequiredMixin, HasCustomerAccessPermission, DetailView):
    template_name = "dashboard/customer/orders/order-invoice.html"
    def get_queryset(self):
        return OrderModel.objects.filter(status=OrderStatusType.success.value)
