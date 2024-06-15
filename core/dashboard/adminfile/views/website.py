from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from dashboard.permissions import HasAdminAccessPermission


class AdminWebsiteView(LoginRequiredMixin,HasAdminAccessPermission,TemplateView):
    template_name = 'dashboard/admin/website/website.html'
