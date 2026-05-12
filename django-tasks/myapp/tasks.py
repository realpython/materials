from django.core.mail import send_mail
from django.tasks import task


@task
def say_hello(name):
    return f"Hello, {name}!"


@task(queue_name="emails", priority=2)
def send_welcome_email(user_id):
    from myapp.models import User

    user = User.objects.get(pk=user_id)
    send_mail(
        subject="Welcome!",
        message="Thanks for joining.",
        from_email=None,
        recipient_list=[user.email],
    )


@task(queue_name="reports", priority=0)
def generate_monthly_report(month):
    return f"report for {month} ready"


@task
def process_order(order_id):
    from myapp.models import Order

    order = Order.objects.get(pk=order_id)
    return f"processed order {order.pk} ({order.item})"
