from django.shortcuts import render
from django.contrib.auth import views as auth_view
from django.views.generic import CreateView,UpdateView,View
from django.urls import reverse_lazy

from .models import *
from .forms import CustomeCreateFrom,CustomeAuthenticationForm


class SignupView(CreateView):
    form_class = CustomeCreateFrom
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')

class CustomLogInView(auth_view.LoginView):
    form_class = CustomeAuthenticationForm
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class CustomLogOutView(auth_view.LogoutView):
    pass

