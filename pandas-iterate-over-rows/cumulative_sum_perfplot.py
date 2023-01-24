import pandas as pd
import perfplot


def loop_cumsum(products):
    cumulative_sum = []
    for product in products.itertuples():
        income = product.sales * product.unit_price
        if cumulative_sum:
            cumulative_sum.append(cumulative_sum[-1] + income)
        else:
            cumulative_sum.append(income)
    return products.assign(cumulative_income=cumulative_sum)


def pandas_cumsum(products):
    return products.assign(
        income=lambda df: df["sales"] * df["unit_price"],
        cumulative_income=lambda df: df["income"].cumsum(),
    ).drop(columns="income")


def get_products(n):
    products = pd.read_csv("resources/products.csv")
    if n < len(products):
        return products.iloc[:n]
    return pd.concat([products for _ in range((n // len(products)) + 1)]).iloc[
        :n
    ]


plot = perfplot.bench(
    n_range=[2**i for i in range(20)],
    setup=get_products,
    kernels=[pandas_cumsum, loop_cumsum],
    labels=["pandas cumsum", "loop cumsum"],
    equality_check=None,
    title="Loop vs Pandas Cumulative Sum",
    xlabel="Number of Rows",
)

plot.show()
