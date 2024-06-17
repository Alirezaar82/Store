from django.views.generic import ListView,UpdateView,View,CreateView,DetailView,DeleteView
from django.core.exceptions import FieldError
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 

from order.models import *
from ..forms import OrderForm

class AdminOrdersListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/orders/order-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = OrderModel.objects.prefetch_related('order_items').all()
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
    
# class AdminOrderDetailView(LoginRequiredMixin, HasAdminAccessPermission, DetailView):
#     template_name = "dashboard/admin/orders/order-detail.html"

#     def get_queryset(self):
#         return OrderModel.objects.all()
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['shippinStatus_form'] = OrderForm()
#         return context
    
class AdminOrderInvoiceView(LoginRequiredMixin, HasAdminAccessPermission, DetailView):
    template_name = "dashboard/admin/orders/order-invoice.html"

    def get_queryset(self):
        return OrderModel.objects.filter(status=OrderStatusType.success.value)

class AdminOrderEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/orders/order-detail.html"
    queryset = OrderModel.objects.all()
    form_class = OrderForm
    success_message = "ویرایش  با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:order-detail", kwargs={"pk": self.get_object().pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = OrderModel.objects.get(id=self.get_object().pk)
        return context
# class AdminOrderEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
#     http_method_names = ['post']
#     queryset = OrderModel.objects.all()
#     form_class = OrderForm
#     success_message = "ویرایش  با موفقیت انجام شد"

#     def get_success_url(self):
#         return reverse_lazy("dashboard:admin:order-detail", kwargs={"pk": self.get_object().pk})