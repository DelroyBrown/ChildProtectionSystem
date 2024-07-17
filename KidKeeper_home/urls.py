from django.urls import path
from . import views


app_name = "KidKeeper_home"

urlpatterns = [
    path("", views.home, name="home"),
]
