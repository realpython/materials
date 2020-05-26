from django.urls import include, path

urlpatterns = [
    path("myapp/", include("myapp.urls")),
]
