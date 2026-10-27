from django.contrib.auth import get_user_model
from django.db import models


class Book(models.Model):
    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text="in cents",
    )
    weight = models.PositiveIntegerField(
        help_text="in grams",
    )

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="naive_cart",
    )
    books = models.ManyToManyField(Book)
