from django.urls import path
from .. import views



urlpatterns = [
    path('security-edit/',views.CustomerChangPasswordView.as_view(),name='security-edit')
]


