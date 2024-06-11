from django.urls import path
from .. import views



urlpatterns = [
    path('security-edit/',views.AdminChangPasswordView.as_view(),name='security-edit')
]


