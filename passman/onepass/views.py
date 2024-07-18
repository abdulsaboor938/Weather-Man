from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


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


def index(request):
    return render(request, "onepass/index.html")
