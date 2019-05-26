from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView
from accounts import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "accounts/profile/",
        login_required(
            TemplateView.as_view(template_name="registration/profile.html")
        ),
        name="profile",
    ),
    path(
        "accounts/edit_profile/",
        views.EditProfileView.as_view(),
        name="edit_profile",
    ),
]
