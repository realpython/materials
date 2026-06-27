from django.urls import path

from myapp import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("task-status/<uuid:task_id>/", views.task_status, name="task_status"),
    path("checkout/", views.checkout, name="checkout"),
]
