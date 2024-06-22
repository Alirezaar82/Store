from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import  SuccessMessageMixin
from django.utils.translation import gettext as _

from dashboard.permissions import HasCustomerAccessPermission
from ..forms import CustomerProfileEditForm,CustomerProfileImageEditForm
from accounts.models import Profile

class CustomerProfileUpdateView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = 'dashboard/customer/profile/profile-edit.html'
    form_class = CustomerProfileEditForm
    success_url = reverse_lazy('dashboard:customer:profile-edit')
    success_message = _('Profile update was successful')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    

class customerProfileImageUpdateView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names = ['post']
    form_class = CustomerProfileImageEditForm
    success_url = reverse_lazy('dashboard:customer:profile-edit')
    success_message = _('image update was successful')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)