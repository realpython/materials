import csv
import random

import faker_commerce
from faker import Faker

fake = Faker()
fake.add_provider(faker_commerce.Provider)

NUMBER_OF_PRODUCTS = 1_000
NUMBER_OF_SALES = 10_000

products = [
    {
        "id": fake.unique.random_int(),
        "name": fake.unique.ecommerce_name(),
        "color": fake.unique.color(),
        "description": fake.text(),
        "price": round(random.random() * 50, 2),
    }
    for _ in range(NUMBER_OF_PRODUCTS)
]

sales = [
    {
        "id": i,
        "product_id": (prod := random.choice(products))["id"],
        "product_name": prod["name"],
        "units_sold": (sold := random.randint(1, 10)),
        "price_paid": round(prod["price"] * sold, 2),
        "customer_name": fake.name(),
    }
    for i in range(10000)
]

with open("products.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=products[0].keys())
    writer.writeheader()

    for product in products:
        writer.writerow(product)

with open("sales.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=sales[0].keys())
    writer.writeheader()

    for sale in sales:
        writer.writerow(sale)
