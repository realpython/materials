from django.contrib import admin
from django.urls import path
from dmd_app.views import markdown_content_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "markdown-content/<slug:slug>/",
        markdown_content_view,
        name="markdown-content",
    ),
]
