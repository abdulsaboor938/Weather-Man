from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("", views.login, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("register/", views.register, name="register"),
    # path("change_password/", views.change_password, name="change_password"),
]
