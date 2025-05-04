# accounts/urls.py
from django.urls import path, include, re_path

# from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from . import views


app_name = "accounts"
urlpatterns = [
    path("", views.CustomUserListView.as_view(), name="users_list"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup-status/<str:status>", views.signup_status_view, name="signup_status"),
    path("activate/<str:uidb64>/<str:token>", views.activate_view, name="activate"),
    path("login/", views.CustomLoginView.as_view()),
    path("users/<int:pk>", views.CustomUserUpdateView.as_view(), name="user_update"),
    path(
        "update_profile/<int:pk>",
        views.CustomUserProfileUpdateView.as_view(),
        name="update_profile",
    ),
]
