from django.views.generic import ListView,UpdateView,TemplateView,CreateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import FieldError
from django.urls import reverse_lazy
from django.shortcuts import redirect


from dashboard.permissions import HasCustomerAccessPermission
from accounts.models import UserAddressModel
from ..forms import UserAddressForm


class CustomerAddressListView(LoginRequiredMixin,HasCustomerAccessPermission,ListView):
    template_name = 'dashboard/customer/addresses/address-list.html'
    def get_queryset(self):
        queryset = UserAddressModel.objects.filter(user=self.request.user)
        if order_by := self.request.GET.get("order_by"):
            try:
                queryset = queryset.order_by(order_by)
            except FieldError:
                pass
        return queryset
    

class CustomerAddressCreateView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, CreateView):
    template_name = "dashboard/customer/addresses/address-create.html"
    
    form_class = UserAddressForm
    success_message = "ایجاد آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:customer:address-edit", kwargs={"pk": form.instance.pk}))
        

    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-list")


class CustomerAddressEditView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/customer/addresses/address-edit.html"
   
    form_class = UserAddressForm
    success_message = "ویرایش آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy("dashboard:customer:address-edit",kwargs={"pk": self.get_object().pk})


class CustomerAddressDeleteView(LoginRequiredMixin, HasCustomerAccessPermission, SuccessMessageMixin, DeleteView):
    template_name = "dashboard/customer/addresses/address-delete.html"
    
    success_url = reverse_lazy("dashboard:customer:address-list")
    success_message = "حذف آدرس با موفقیت انجام شد"

    def get_queryset(self):
        return UserAddressModel.objects.filter(user=self.request.user)
