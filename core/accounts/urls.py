from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('login/',views.CustomLogInView.as_view(),name='login'),
    path('logout/',views.CustomLogOutView.as_view(),name='logout'),
] 