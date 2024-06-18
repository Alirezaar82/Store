from django.views.generic import ListView,UpdateView,CreateView,DetailView,DeleteView
from django.core.exceptions import FieldError
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 

from order.models import CouponModel
from ..forms import CouponForm
from dashboard.permissions import HasAdminAccessPermission


class AdminCouponListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/coupons/coupon-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = CouponModel.objects.all()
        if search_q := self.request.GET.get('q'):
            queryset = queryset.filter(code__icontains=search_q)
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        return context
    

class AdminCouponDetailView(LoginRequiredMixin,HasAdminAccessPermission,DetailView):
    template_name = 'dashboard/admin/coupons/coupon-detail.html'
    queryset = CouponModel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AdminCouponEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/coupons/coupon-edit.html"
    queryset = CouponModel.objects.all()
    form_class = CouponForm
    success_message = "ویرایش کد تخفیف با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-edit", kwargs={"pk": self.get_object().pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AdminCouponCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/coupons/coupon-create.html"
    queryset = CouponModel.objects.all()
    form_class = CouponForm
    success_message = "ایجاد کد تخفیف با موفقیت انجام شد"

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:coupon-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:coupon-list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class AdminCouponDeleteview(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/coupons/coupon-delete.html"
    queryset = CouponModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:coupon-list")
    success_message = "حذف کد تخفیف با موفقیت انجام شد"

