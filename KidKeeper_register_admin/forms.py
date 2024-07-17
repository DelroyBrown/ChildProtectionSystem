# KidKeeper_register_admin/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterAdminWorker


class AdminWorkerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=25, required=False)
    address = forms.CharField(max_length=255, required=False)
    date_of_birth = forms.DateField(
        required=False, widget=forms.SelectDateWidget(years=range(1900, 2100))
    )

    class Meta:
        model = RegisterAdminWorker
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "date_of_birth",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
