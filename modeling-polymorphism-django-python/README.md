# Modeling Polymorphism in Django With Python

This folder provides the code examples for the Real Python tutorial [Modeling Polymorphism in Django With Python](https://realpython.com/modeling-polymorphism-django-python/).

The code is a runnable Django project called `bookstore`, with one Django app per modeling technique covered in the tutorial. It requires Python 3.12 or later, which is the minimum version supported by Django 6.1.

## Installation

Create and activate a virtual environment, install Django, and create the database tables:

```console
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
(venv) $ python manage.py migrate
```

The project uses SQLite, so you don't need a database server. The tutorial recommends PostgreSQL, but every example also works on SQLite. In particular, Django's built-in `models.JSONField`, used by the semi-structured model, supports SQLite, including key lookups like `extra__weight__gt=100`. To use PostgreSQL instead, install `psycopg` and change `DATABASES` in `bookstore/settings.py`.

## Apps

Each app maps to a section of the tutorial:

| App | Tutorial section | Models |
| --- | --- | --- |
| `naive/` | Naive Implementation | `Book`, `Cart` |
| `sparse/` | Sparse Model | `Book` with a `type` field and `clean()` validation, `Cart` |
| `semi_structured/` | Semi-Structured Model | `Book` with an `extra` `JSONField` and `clean()` validation, `Cart` |
| `abstract_base_model/` | Abstract Base Model | Abstract `Product`, `Book`, `EBook`, `Cart` with one many-to-many field per product type |
| `concrete_base_model/` | Concrete Base Model | Concrete `Product`, `Book`, `EBook`, `Cart` with a many-to-many field to `Product` |
| `generic_foreign_key/` | Generic Foreign Key | `Product` protocol, `Book` with a `GenericRelation`, `EBook`, `Cart` with `add_item()`, `CartItem` with a `GenericForeignKey` |

All apps share Django's built-in user model. Because each app defines a `Cart` with a one-to-one field to the user, each of these fields has an app-specific `related_name`, like `"naive_cart"`, to avoid clashing reverse accessors.

## Usage

Open a Django shell with `python manage.py shell` and follow along with the tutorial. For example:

```pycon
>>> from django.contrib.auth import get_user_model
>>> user = get_user_model().objects.create_user("haki")

>>> from concrete_base_model.models import Book, EBook, Cart
>>> book = Book.objects.create(name="Python Tricks", price=1000, weight=200)
>>> ebook = EBook.objects.create(
...     name="The Old Man and the Sea",
...     price=1500,
...     download_link="http://books.com/12345",
... )
>>> cart = Cart.objects.create(user=user)
>>> cart.items.add(book, ebook)
>>> cart.items.all()
<QuerySet [<Product: Python Tricks>, <Product: The Old Man and the Sea>]>

>>> from django.db.models import Sum
>>> cart.items.aggregate(total_price=Sum("price"))
{'total_price': 2500}
```

To start over with an empty database, delete `db.sqlite3` and run `python manage.py migrate` again.
