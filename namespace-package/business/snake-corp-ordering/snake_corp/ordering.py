import csv
import os
from importlib import resources

from snake_corp import dateutil

import requests

CONFIDENTIAL_API_ENDPOINT = "https://httpbin.org/post"


def read_products():
    with resources.open_text("snake_shop", "products.csv") as f:
        return list(csv.DictReader(f))


def get_product_by_id(id, products=None):
    if products is None:
        products = read_products()

    return next(product for product in products if product["id"] == id)


def make_order(product_id, quantity):
    os.environ.get("SNAKE_CORP_ORDERING_KEY")
    resp = requests.post(
        CONFIDENTIAL_API_ENDPOINT,
        json={"id": product_id, "quantity": quantity},
    )
    if resp.status_code == 200:
        print("order success")
    else:
        print("something went wrong")
