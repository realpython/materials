from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.listing, name="listing"),
    path("view_blog/<int:blog_id>/", core_views.view_blog, name="view_blog"),
    path("see_request/", core_views.see_request),
    path("user_info/", core_views.user_info),
    path("private_place/", core_views.private_place),
    path("accounts/", include("django.contrib.auth.urls")),
    path("staff_place/", core_views.staff_place),
    path("add_messages/", core_views.add_messages),
]
