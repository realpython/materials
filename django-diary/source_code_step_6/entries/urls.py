from django.urls import path

from . import views

urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path(
        "entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
]
