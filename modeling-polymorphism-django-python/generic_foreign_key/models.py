from typing import Protocol

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Product(Protocol):
    pk: int
    name: str
    price: int

    def __str__(self) -> str: ...


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
    cart_items = GenericRelation(
        "CartItem",
        "product_object_id",
        "product_content_type_id",
        related_query_name="books",
    )

    def __str__(self) -> str:
        return self.name


class EBook(models.Model):
    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text="in cents",
    )
    download_link = models.URLField()

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="generic_foreign_key_cart",
    )

    def add_item(
        self,
        product: Product,
    ) -> "CartItem":
        product_content_type = ContentType.objects.get_for_model(product)

        return CartItem.objects.create(
            cart=self,
            product_content_type=product_content_type,
            product_object_id=product.pk,
        )


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product_object_id = models.IntegerField()
    product_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
    )
    product = GenericForeignKey(
        "product_content_type",
        "product_object_id",
    )
