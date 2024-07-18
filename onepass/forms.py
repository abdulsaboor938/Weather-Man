from django import forms
from .models import Password
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ["website", "username", "password"]


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Old Password"})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "New Password"})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm New Password"})
    )

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
