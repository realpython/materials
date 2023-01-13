import codetiming
import pandas as pd


def loop_cumsum(products):
    cumulative_sum = []
    for row in products.itertuples():
        if cumulative_sum:
            cumulative_sum.append(
                cumulative_sum[-1] + (row.sales * row.unit_price)
            )
        else:
            cumulative_sum.append(row.sales * row.unit_price)
    return products.assign(cumulative_income=cumulative_sum)


def pandas_cumsum(products):
    return products.assign(
        income=lambda df: df["sales"] * df["unit_price"],
        cumulative_income=lambda df: df["income"].cumsum(),
    ).drop(columns="income")


for f in [pandas_cumsum, loop_cumsum]:
    products = pd.read_csv("resources/products.csv")
    products = pd.concat(products for _ in range(1000))
    with codetiming.Timer(
        name=f.__name__, text="{name:20}: {milliseconds:.2f} ms"
    ):
        f(products)
