from django.shortcuts import redirect
from django.views.generic import TemplateView,CreateView
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class ContactUsView(TemplateView):
    template_name = 'website/contact-us.html'
  

class SendContactView(CreateView):
    
    http_method_names = ['post']
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'تیکت شما با موفقیت ثبت شد و در اسرع وقت با شما تماس و یا در ایمیل پاسخ داده خواهد شد')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'مشکلی در ارسال فرم شما پیش آمد لطفا ورودی ها رو بررسی کنین و مجدد ارسال نمایید')
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')