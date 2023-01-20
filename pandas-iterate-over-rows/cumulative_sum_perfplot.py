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


products = pd.read_csv("resources/products.csv")

plot = perfplot.bench(
    n_range=[i**2 for i in range(1, 1000, 100)],
    setup=lambda n: pd.concat([products for _ in range(n)]),
    kernels=[pandas_cumsum, loop_cumsum],
    labels=["pandas cumsum", "loop cumsum"],
    equality_check=None,
)

plot.show()
plot.show(logy=True)
