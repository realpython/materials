from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.projects.urls")),
    path("blog/", include("apps.blog.urls")),
    path("contact/", include("apps.contact.urls")),
]
