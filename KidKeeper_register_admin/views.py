# KidKeeper_register_admin/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import AdminWorkerRegistrationForm


def register_admin_worker(request):
    if request.method == "POST":
        form = AdminWorkerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("KidKeeper_dashboard:admin-dashboard")
    else:
        form = AdminWorkerRegistrationForm()
    return render(request, "admin/admin_registration/register.html", {"form": form})


def logout_confirmation(request):
    return render(request, "admin/admin_registration/admin_logout_confirmation.html")


def perform_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("KidKeeper_register_admin:login")
    else:
        return redirect("KidKeep_dashboard:admin-dashboard")


def custom_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("KidKeeper_dashboard:admin-dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "admin/admin_registration/login.html", {"form": form})
