from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import  SuccessMessageMixin
from django.utils.translation import gettext as _

from dashboard.permissions import HasAdminAccessPermission
from ..forms import AdminProfileEditForm,AdminProfileImageEditForm
from accounts.models import Profile

class AminProfileUpdateView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    template_name = 'dashboard/admin/profile/profile-edit.html'
    form_class = AdminProfileEditForm
    success_url = reverse_lazy('dashboard:admin:profile-edit')
    success_message = _('Profile update was successful')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    

class AdminProfileImageUpdateView(LoginRequiredMixin,HasAdminAccessPermission,SuccessMessageMixin,UpdateView):
    http_method_names = ['post']
    form_class = AdminProfileImageEditForm
    success_url = reverse_lazy('dashboard:admin:profile-edit')
    success_message = _('image update was successful')

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)