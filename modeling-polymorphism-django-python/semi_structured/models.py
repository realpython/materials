from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
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

    extra = models.JSONField()

    def __str__(self) -> str:
        return f"[{self.get_type_display()}] {self.name}"

    def clean(self) -> None:
        if self.type == Book.TYPE_VIRTUAL:
            try:
                weight = int(self.extra["weight"])
            except ValueError:
                raise ValidationError("Weight must be a number")
            except KeyError:
                pass
            else:
                if weight != 0:
                    raise ValidationError(
                        "A virtual product weight cannot exceed zero."
                    )

            try:
                download_link = self.extra["download_link"]
            except KeyError:
                pass
            else:
                # Will raise a validation error
                URLValidator()(download_link)

        elif self.type == Book.TYPE_PHYSICAL:
            try:
                weight = int(self.extra["weight"])
            except ValueError:
                raise ValidationError("Weight must be a number")
            except KeyError:
                pass
            else:
                if weight == 0:
                    raise ValidationError(
                        "A physical product weight must exceed zero."
                    )

            try:
                download_link = self.extra["download_link"]
            except KeyError:
                pass
            else:
                if download_link is not None:
                    raise ValidationError(
                        "A physical product cannot have a download link."
                    )

        else:
            raise ValidationError(f'Unknown product type "{self.type}"')


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="semi_structured_cart",
    )
    books = models.ManyToManyField(
        Book,
        related_name="+",
    )
