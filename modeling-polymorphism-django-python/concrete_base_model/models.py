from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text="in cents",
    )

    def __str__(self) -> str:
        return self.name


class Book(Product):
    weight = models.PositiveIntegerField()


class EBook(Product):
    download_link = models.URLField()


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="concrete_base_model_cart",
    )
    items = models.ManyToManyField(Product)
