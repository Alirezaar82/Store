from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import  SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib.auth import views as auth_view

from dashboard.permissions import HasAdminAccessPermission
from ..forms import AdminPasswordChangeForm 
from accounts.models import Profile

class AdminChangPasswordView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,auth_view.PasswordChangeView):
    template_name = 'dashboard/admin/security/security-edit.html'
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy('dashboard:admin:security-edit')
    success_message = _('"Password update was successful"')
