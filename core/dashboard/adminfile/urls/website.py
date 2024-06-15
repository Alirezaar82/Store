from django.urls import path
from .. import views



urlpatterns = [
    path('website/',views.AdminWebsiteView.as_view(),name='website'),
]


