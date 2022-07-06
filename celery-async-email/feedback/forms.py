# TODO: Adapt the imports when moving the email sending code
from time import sleep

from django.core.mail import send_mail
from django import forms

from feedback.tasks import send_feedback_email_task


class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 5}))

    def send_email(self, email_address, message):

        # TODO: Initial project state handles email sending right here
        # then I show how that freezes the Django app, then show as a solution
        # how to move it over to a Celery task and how that frees up Django

        # sleep(20)  # Simulate expensive operation that freezes Django
        # send_mail(
        #     "Your Feedback",
        #     f"\t{message}\n\nThank you for your feedback.",
        #     "support@yourdomain.com",
        #     [email_address],
        #     fail_silently=False
        # )

        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
