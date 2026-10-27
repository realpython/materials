from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=100,
    )
    price = models.PositiveIntegerField(
        help_text="in cents",
    )

    def __str__(self) -> str:
        return self.name


class Book(Product):
    weight = models.PositiveIntegerField(
        help_text="in grams",
    )


class EBook(Product):
    download_link = models.URLField()


# A ManyToManyField to the abstract Product model doesn't work:
#
#     items = models.ManyToManyField(Product)
#
# abstract_base_model.Cart.items: (fields.E300) Field defines a relation
# with model 'Product', which is either not installed, or is abstract.
#
# Instead, the cart references books and e-books directly:
class Cart(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="abstract_base_model_cart",
    )
    books = models.ManyToManyField(Book)
    ebooks = models.ManyToManyField(EBook)
