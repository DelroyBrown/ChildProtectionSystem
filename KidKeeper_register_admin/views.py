# KidKeeper_register_admin/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
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
    return render(request, "admin_registration/register.html", {"form": form})
