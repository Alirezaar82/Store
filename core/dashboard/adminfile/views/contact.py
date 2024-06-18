from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F,Q
from django.core import exceptions

from dashboard.permissions import HasAdminAccessPermission
from website.models import ContactUsModel

class AdminContactUsListView(LoginRequiredMixin,HasAdminAccessPermission,ListView):
    template_name = 'dashboard/admin/contacts/contact-list.html'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.paginate_by)
    
    def get_queryset(self):
        queryset = ContactUsModel.objects.all()
        search_query = self.request.GET.get('q', None)
        ordering_query = self.request.GET.get('ordering', None)

        if search_query:
            queryset = queryset.filter(
                 Q(email__icontains=search_query) |
                 Q(subject__icontains=search_query) |
                 Q(content__icontains=search_query) |
                 Q(phone_number__icontains=search_query)
            )
        if ordering_query:
            try:
                queryset = queryset.order_by(ordering_query)
            except exceptions.FieldError:
                pass
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        return context


class AdminContactUsDetailView(LoginRequiredMixin,HasAdminAccessPermission,DetailView):
    template_name = 'dashboard/admin/contacts/contact-detail.html'
    queryset = ContactUsModel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context