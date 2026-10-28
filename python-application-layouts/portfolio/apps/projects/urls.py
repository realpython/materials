from django.urls import path

from apps.projects import views

app_name = "projects"
urlpatterns = [
    path("", views.index, name="index"),
]
