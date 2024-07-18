from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="home"),
    path("", views.login, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("add-password/", views.add_password, name="add_password"),
    path("edit-password/<int:pk>/", views.edit_password, name="edit_password"),
    path("delete-password/<int:pk>/", views.delete_password, name="delete_password"),
    path("edit-password/<int:pk>/", views.edit_password, name="edit_password"),
    path("delete-password/<int:pk>/", views.delete_password, name="delete_password"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("register/", views.register, name="register"),
    # path("change_password/", views.change_password, name="change_password"),
]
