from django.views.generic import ListView,UpdateView,View,CreateView,DetailView,DeleteView
from django.core.exceptions import FieldError
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

from shop.models import *
from shop.forms import *
from ..forms import ProductForm

class AdminProductsListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/products/product-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ProductModel.objects.prefetch_related('category').all()
        if search_q := self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=search_q)
        if category_id := self.request.GET.get('category_id'):
            queryset = queryset.filter(category__id=category_id)
        if min_price := self.request.GET.get('min_price'):
            queryset = queryset.filter(price__gte=min_price).order_by('price')
        if max_price := self.request.GET.get('max_price'):
            queryset = queryset.filter(price__lte=max_price).order_by('-price')
        if order_by := self.request.GET.get('order_by'):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass 

        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.all()
        context['total_items'] = self.get_queryset().count()
        context['total_items_published'] = self.get_queryset().filter(status=ProductStatusType.publish.value).count()
        return context
    

class AdminProductDetailView(LoginRequiredMixin,HasAdminAccessPermission,DetailView):
    template_name = 'dashboard/admin/products/product-detail.html'
    queryset = ProductModel.objects.prefetch_related('category').all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["is_wished"] = WishlistProductModel.objects.filter(
            user=self.request.user, product__id=product.id).exists() if self.request.user.is_authenticated else False
        reviews = ReviewModel.objects.filter(product=product,status=ReviewStatusType.accepted.value)
        context["reviews"] = reviews
        total_reviews_count =reviews.count()
        context["reviews_count"] = {
            f"rate_{rate}": reviews.filter(rate=rate).count() for rate in range(1, 6)
        }
        if total_reviews_count != 0:
            context["reviews_avg"] = {
                f"rate_{rate}": round((reviews.filter(rate=rate).count()/total_reviews_count)*100,2) for rate in range(1, 6)
            }
        else:
            context["reviews_avg"] = {f"rate_{rate}": 0 for rate in range(1, 6)}
        return context
    
class AdminProductEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/products/product-edit.html"
    queryset = ProductModel.objects.prefetch_related('category').all()
    form_class = ProductForm
    success_message = "ویرایش محصول با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:product-edit", kwargs={"pk": self.get_object().pk})
    
class AdminProductCreateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/admin/products/product-create.html"
    queryset = ProductModel.objects.all()
    form_class = ProductForm
    success_message = "ایجاد محصول با موفقیت انجام شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:admin:product-edit", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:products-list")
    
class AdminProductDeleteview(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/admin/products/product-delete.html"
    queryset = ProductModel.objects.all()
    success_url = reverse_lazy("dashboard:admin:products-list")
    success_message = "حذف محصول با موفقیت انجام شد"
