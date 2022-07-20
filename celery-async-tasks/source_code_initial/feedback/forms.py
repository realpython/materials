from time import sleep

from django import forms
from django.core.mail import send_mail


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        sleep(20)  # Simulate expensive operation that freezes Django
        send_mail(
            "Your Feedback",
            f"\t{self.cleaned_data['message']}\n\nThank you!",
            "support@example.com",
            [self.cleaned_data["email"]],
            fail_silently=False,
        )
