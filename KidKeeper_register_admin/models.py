# KidKeeper_register_admin/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class RegisterAdminWorker(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Admin Worker"
        verbose_name_plural = "Admin Workers"
