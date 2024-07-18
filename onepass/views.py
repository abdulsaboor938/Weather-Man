from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Password
from .forms import PasswordForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def login(request):
    username = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")  # Redirect to the index page after successful login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "onepass/login.html", {"username": username})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        else:
            user = User.objects.create_user(username=username, password=password1)
            messages.success(request, f"Account created for {username}")
            return redirect("login")

    return render(request, "onepass/signup.html")


@login_required
def index(request):
    passwords = Password.objects.filter(user=request.user)
    return render(
        request,
        "onepass/index.html",
        {"passwords": passwords, "username": request.user.username},
    )


@login_required
def add_password(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.save(commit=False)
            password.user = request.user
            password.save()
            messages.success(request, "Password added successfully.")
            return redirect("home")
    else:
        form = PasswordForm()
    return render(request, "onepass/add_password.html", {"form": form})


@login_required
def edit_password(request, pk):
    password = get_object_or_404(Password, pk=pk, user=request.user)
    if request.method == "POST":
        form = PasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated successfully.")
            return redirect("home")
    else:
        form = PasswordForm(instance=password)
    return render(request, "onepass/edit_password.html", {"form": form})


@login_required
def delete_password(request, pk):
    password = get_object_or_404(Password, pk=pk, user=request.user)
    if request.method == "POST":
        password.delete()
        messages.success(request, "Password deleted successfully.")
        return redirect("home")
    return render(request, "onepass/delete_password.html", {"password": password})


def logout_view(request):
    auth_logout(request)
    return redirect("login")


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Important to keep the user logged in
            messages.success(request, "Your password was successfully updated!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "onepass/edit_profile.html", {"form": form})
