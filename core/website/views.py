from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class ContactUsView(TemplateView):
    template_name = 'website/contact-us.html'
