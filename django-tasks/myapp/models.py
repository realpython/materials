from django.db import models


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.email


class Order(models.Model):
    item = models.CharField(max_length=100, default="widget")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.pk} ({self.item})"
