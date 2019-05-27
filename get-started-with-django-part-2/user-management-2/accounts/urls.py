from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [
    path("login/", views.LogInView.as_view(), name="login"),
    path("logout/", views.LogOutView.as_view(), name="logout"),
    path(
        "password_change/",
        login_required(views.PasswordChangeView.as_view()),
        name="password_change",
    ),
    path(
        "password_change_done/",
        login_required(
            TemplateView.as_view(
                template_name="registration/password_change_done.html"
            )
        ),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        TemplateView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/confirm",
        TemplateView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
