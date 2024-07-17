from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "KidKeeper_register_admin"

urlpatterns = [
    path(
        "register/register_admin",
        views.register_admin_worker,
        name="register-admin-worker",
    ),
    path("login/", views.custom_login_view, name="login"),
    path("logout/", views.logout_confirmation, name="logout_confirmation"),
    path("perform_logout/", views.perform_logout, name="perform_logout"),
]
