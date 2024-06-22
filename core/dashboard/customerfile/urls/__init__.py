from django.urls import path,include

app_name = "customer"

urlpatterns = [
    path("",include("dashboard.customerfile.urls.home")),
    path("",include("dashboard.customerfile.urls.address")),
    path("",include("dashboard.customerfile.urls.profile")),
    path("",include("dashboard.customerfile.urls.security")),
    path("",include("dashboard.customerfile.urls.order")),
    path("",include("dashboard.customerfile.urls.wishlist")),
]
