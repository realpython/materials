from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form had been submitted."""

    sleep(20)  # Simulate expensive operation that freezes Django
    # TODO: Maybe show a real example, e.g. comment moderation or
    #       text translation

    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you for your feedback.",
        "support@yourdomain.com",
        [email_address],
        fail_silently=False,
    )

    # TODO: should there be a return value? What's best practice?
    # return "OK"
