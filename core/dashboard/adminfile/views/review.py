from django.views.generic import ListView,UpdateView,View,CreateView,DetailView,DeleteView
from django.core.exceptions import FieldError
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 

from shop.models import ReviewModel,ReviewStatusType
from ..forms import ReviewForm

class AdminReviewListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/review/review-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ReviewModel.objects.all()
        if search_q := self.request.GET.get("q"):
            queryset = queryset.filter(product__title__icontains=search_q)
        if status := self.request.GET.get("status"):
            queryset = queryset.filter(status=status)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        context['total_items_published'] = self.get_queryset().filter(status=ReviewStatusType.accepted).count()
        context['status_types'] = ReviewStatusType.choices
        return context
    


    
class AdminReviewEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/review/review-edit.html"
    queryset = ReviewModel.objects.all()
    form_class = ReviewForm
    success_message = "ویرایش دیدگاه با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:review-edit", kwargs={"pk": self.get_object().pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = ReviewModel.objects.get(id=self.get_object().pk)
        return context
    
    
class AdminReviewDeleteview(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/review/review-delete.html"
    queryset = ReviewModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:review-list")
    success_message = "حذف دیدگاه با موفقیت انجام شد"
