# KidKeeper_dashboard/urls.py
from django.urls import path
from . import views

app_name = "KidKeeper_dashboard"

urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard'),
]
