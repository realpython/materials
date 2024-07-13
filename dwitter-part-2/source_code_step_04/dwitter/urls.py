from django.urls import path

from .views import dashboard

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
