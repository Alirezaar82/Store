from django.forms import BaseModelForm
from django.views.generic import ListView,DetailView,View,CreateView
from django.core.exceptions import FieldError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import *
from .forms import ReviewForm

class ProductsGridView(ListView):
    template_name = 'shop/products-grid.html'
    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ProductModel.objects.prefetch_related('category').filter(
            stock__gte=1,
            status=ProductStatusType.publish.value
            )
        if search_q := self.request.GET.get('q'):
            queryset = queryset.filter(title__icontains=search_q)
        if category := self.request.GET.get('category_slug'):
            queryset = queryset.filter(category__slug=category)
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
        context['wishlist_items'] = WishlistProductModel.objects.filter(user=self.request.user).values_list(
            "product__id", flat=True) if self.request.user.is_authenticated else []
        return context
    
class ProductDetailView(DetailView):
    template_name = 'shop/product-detail.html'
    queryset = ProductModel.objects.prefetch_related('category').filter(
            stock__gte=1,
            status=ProductStatusType.publish.value
            )
    
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

    

class AddOrRemoveWishlistProductView(LoginRequiredMixin,View):

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        message = ''
        if product_id:
            try:
               item =  WishlistProductModel.objects.get(user=request.user,product__id=product_id)
               item.delete()
               message = _('item has been removed')
            except WishlistProductModel.DoesNotExist:
                WishlistProductModel.objects.create(
                    user=request.user,
                    product_id=product_id
                )
                message = _('item has been added')
        return JsonResponse({'message':message})
    
class SubmitReviewView(LoginRequiredMixin,CreateView):
    http_method_names = ["post"]
    model = ReviewModel
    form_class = ReviewForm
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        form.save()
        product = form.cleaned_data['product']

        messages.success(self.request,_('Your comment has been successfully submitted and will be displayed after review'))
        return redirect(reverse_lazy('shop:product-detail',kwargs={"slug":product.slug}))
    
    def form_invalid(self, form: BaseModelForm):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request,error)
        return redirect(self.request.META.get('HTTP_REFERER'))
    
    def get_queryset(self):
        # You can customize the queryset if needed
        return ReviewModel.objects.filter(user=self.request.user)

        

