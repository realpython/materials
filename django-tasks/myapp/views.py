from functools import partial

from django.db import transaction
from django.http import JsonResponse
from django.tasks import default_task_backend, TaskResultStatus

from myapp.models import Order, User
from myapp.tasks import process_order, send_welcome_email


def register(request):
    user = User.objects.create(
        email=request.GET.get("email", "demo@example.com"),
        name=request.GET.get("name", "Demo"),
    )
    result = send_welcome_email.enqueue(user.id)
    return JsonResponse({"task_id": str(result.id), "user_id": user.id})


def task_status(request, task_id):
    result = default_task_backend.get_result(task_id)
    result.refresh()
    if result.status == TaskResultStatus.SUCCESSFUL:
        return JsonResponse({"status": "done", "value": result.return_value})
    if result.is_finished:
        return JsonResponse({"status": "failed"})
    return JsonResponse({"status": "pending"})


def checkout(request):
    with transaction.atomic():
        order = Order.objects.create()
        transaction.on_commit(
            partial(process_order.enqueue, order.id)
        )
    return JsonResponse({"order_id": order.id})
