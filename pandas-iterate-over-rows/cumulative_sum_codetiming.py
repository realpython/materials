import pandas as pd
from codetiming import Timer


def loop_cumsum(products):
    cumulative_sum = []
    for product in products.itertuples():
        if cumulative_sum:
            cumulative_sum.append(
                cumulative_sum[-1] + (product.sales * product.unit_price)
            )
        else:
            cumulative_sum.append(product.sales * product.unit_price)
    return products.assign(cumulative_income=cumulative_sum)


def pandas_cumsum(products):
    return products.assign(
        income=lambda df: df["sales"] * df["unit_price"],
        cumulative_income=lambda df: df["income"].cumsum(),
    ).drop(columns="income")


for func in [loop_cumsum, pandas_cumsum]:
    products = pd.read_csv("resources/products.csv")
    products = pd.concat(products for _ in range(1000))
    with Timer(name=func.__name__, text="{name:20}: {milliseconds:.2f} ms"):
        func(products)
