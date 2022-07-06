from django import forms
from django.core.mail import send_mail

from feedback.tasks import send_feedback_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5}))

    def send_email(self):
        send_mail(
            "Your Feedback",
            "We've received your feedback. This is a copy. Feel free to respond to this thread.",
            "support@yourdomain.com",
            ["you@yourdomain.com"],
            fail_silently=False
        )

        # send_feedback_email_task.delay(
        #     self.cleaned_data["email"], self.cleaned_data["message"]
        # )
