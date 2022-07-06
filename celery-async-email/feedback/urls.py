from django.urls import path

from feedback.views import FeedbackFormView

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
]