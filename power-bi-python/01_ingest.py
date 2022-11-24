import sqlite3

import pandas as pd

with sqlite3.connect(r"C:\<YOUR_PATH_TO_DB>\car_sales.db") as connection:
    df = pd.read_sql_query("SELECT * FROM sales", connection)

cars = df[
    [
        "vin",
        "car",
        "mileage",
        "license",
        "color",
        "purchase_date",
        "purchase_price",
        "investment",
    ]
]
customers = df[["vin", "customer"]]
sales = df[["vin", "sale_price", "sale_date"]]
