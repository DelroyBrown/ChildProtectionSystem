from django.urls import path
from . import views

app_name = "KidKeeper_register_admin"

urlpatterns = [
    path(
        "register/register_admin",
        views.register_admin_worker,
        name="register-admin-worker",
    ),
]
