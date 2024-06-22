from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import  SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth import views as auth_view

from dashboard.permissions import HasCustomerAccessPermission
from ..forms import CustomerPasswordChangeForm 
from accounts.models import Profile

class CustomerChangPasswordView(LoginRequiredMixin,HasCustomerAccessPermission,SuccessMessageMixin,auth_view.PasswordChangeView):
    template_name = 'dashboard/customer/profile/security-edit.html'
    form_class = CustomerPasswordChangeForm
    success_url = reverse_lazy('dashboard:customer:security-edit')
    success_message = _('"Password update was successful"')
