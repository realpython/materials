from celery import shared_task


@shared_task()
def send_feedback_email_task(email, message):
    """Sends an email when the feedback form is filled correctly and submitted successfully."""
    return
    # return send_feedback_email(email, message)