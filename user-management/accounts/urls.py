from django.urls import path, include

from accounts import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.SignUp.as_view(), name="signup"),
]
