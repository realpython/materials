from django.urls import path

from .views import PhotoView

app_name = "photos"

urlpatterns = [
    path("", PhotoView.as_view(), name="photoview"),
]
