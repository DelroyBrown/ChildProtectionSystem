from django.contrib import admin
from django.urls import path, include

app_name = "KidKeeper_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("KidKeeper_home.urls")),
    path("", include("KidKeeper_register_admin.urls")),
    path("dashboard/", include("KidKeeper_dashboard.urls")),
]
