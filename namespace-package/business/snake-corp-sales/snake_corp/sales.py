import csv
from importlib import resources


def read_products():
    with resources.open_text("snake_corp", "sales.csv") as f:
        return list(csv.DictReader(f))


def get_sales_by_product_id(product_id, sales=None):
    if sales is None:
        sales = read_products()

    return [sale for sale in sales if sale["product_id"] == product_id]
