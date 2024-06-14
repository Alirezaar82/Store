from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.core.exceptions import FieldError
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

from shop.models import ProductCategoryModel ,ProductModel
from dashboard.permissions import HasAdminAccessPermission
from ..forms import CategoryForm


class AdminCategoryListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/category/category-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ProductCategoryModel.objects.all()
        if search_q := self.request.GET.get('q'):
            queryset = queryset.filter(name__icontains=search_q)
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        category_product_counts = {}
        categoris = self.get_queryset()
        for category in categoris:
            published_count = ProductModel.objects.filter(
                category=category,
            ).count()
            category_product_counts[category.id] = published_count        
        context['category_product_counts'] = category_product_counts
        return context
    
class AdminCategoryEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/category/category-edit.html"
    queryset = ProductCategoryModel.objects.all()
    form_class = CategoryForm
    success_message = "ویرایش دسته بندی با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:category-edit", kwargs={"pk": self.get_object().pk})
    
class AdminCategoryCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/category/category-create.html"
    queryset = ProductModel.objects.all()
    form_class = CategoryForm
    success_message = "ایجاد دسته بندی با موفقیت انجام شد"

    def form_valid(self, form):
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:category-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:category-list")
    
class AdminCategoryDeleteview(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/category/category-delete.html"
    queryset = ProductCategoryModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:category-list")
    success_message = "حذف دسته بندی با موفقیت انجام شد"
