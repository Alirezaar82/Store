from django.urls import path,include

app_name = "admin"

urlpatterns = [
    path("",include("dashboard.adminfile.urls.home")),
    path("",include("dashboard.adminfile.urls.profile")),
    path("",include("dashboard.adminfile.urls.security")),
    path("",include("dashboard.adminfile.urls.product")),
    path("",include("dashboard.adminfile.urls.category")),
    path("",include("dashboard.adminfile.urls.logo")),
    path("",include("dashboard.adminfile.urls.website")),
]
