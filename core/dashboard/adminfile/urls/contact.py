from django.urls import path
from .. import views



urlpatterns = [
    path('contact-list/',views.AdminContactUsListView.as_view(),name='contact-list'),
    path('contact/<int:pk>/detail/',views.AdminContactUsDetailView.as_view(),name='contact-detail'),
]


