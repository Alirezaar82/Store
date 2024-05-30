from django.views.generic import ListView,DetailView
from django.core.exceptions import FieldError

from .models import *

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
        return context
    
class ProductDetailView(DetailView):
    template_name = 'shop/product-detail.html'
    queryset = ProductModel.objects.prefetch_related('category').filter(
            stock__gte=1,
            status=ProductStatusType.publish.value
            )