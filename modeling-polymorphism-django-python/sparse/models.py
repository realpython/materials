from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


class Book(models.Model):
    TYPE_PHYSICAL = "physical"
    TYPE_VIRTUAL = "virtual"
    TYPE_CHOICES = (
        (TYPE_PHYSICAL, "Physical"),
        (TYPE_VIRTUAL, "Virtual"),
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    # Common attributes
    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text="in cents",
    )

    # Specific attributes
    weight = models.PositiveIntegerField(
        help_text="in grams",
    )
    download_link = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"[{self.get_type_display()}] {self.name}"

    def clean(self) -> None:
        if self.type == Book.TYPE_VIRTUAL:
            if self.weight != 0:
                raise ValidationError(
                    "A virtual product weight cannot exceed zero."
                )

            if self.download_link is None:
                raise ValidationError(
                    "A virtual product must have a download link."
                )

        elif self.type == Book.TYPE_PHYSICAL:
            if self.weight == 0:
                raise ValidationError(
                    "A physical product weight must exceed zero."
                )

            if self.download_link is not None:
                raise ValidationError(
                    "A physical product cannot have a download link."
                )

        else:
            assert False, f'Unknown product type "{self.type}"'


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="sparse_cart",
    )
    books = models.ManyToManyField(
        Book,
    )
