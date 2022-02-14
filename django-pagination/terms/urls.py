from django.urls import path
from . import views

urlpatterns = [
    path(
        "all", views.AllKeywordsView.as_view(template_name="terms/base.html")
    ),
]
