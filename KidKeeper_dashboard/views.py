# KidKeeper_dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_dashboard(request):
    admin_worker_user = request.user
    return render(
        request,
        "admin/admin_dashboard/admin_dashboard.html",
        {"admin_worker_user": admin_worker_user},
    )
