from django.urls import path,include

app_name = "customer"

urlpatterns = [
    path("",include("dashboard.customerfile.urls.home")),
]
