from django.urls import path

from feedback.views import IndexView, FeedbackFormView, SuccessView

app_name = "feedback"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
]
