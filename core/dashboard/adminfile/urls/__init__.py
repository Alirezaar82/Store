from django.urls import path,include

app_name = "admin"

urlpatterns = [
    path("",include("dashboard.adminfile.urls.home")),
    path("",include("dashboard.adminfile.urls.profile")),
]
