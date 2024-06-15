from django.views.generic import UpdateView
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from website.models import *
from ..forms import LogoForm


class AdminLogoEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/website/logo-edit.html"
    queryset = LogoModel.objects.all()
    form_class = LogoForm
    success_message = "ویرایش لوگو سایت با موفقیت انجام شد"

    def get_success_url(self):
        return reverse_lazy("dashboard:admin:logo-edit", kwargs={"pk": self.get_object().pk})
    