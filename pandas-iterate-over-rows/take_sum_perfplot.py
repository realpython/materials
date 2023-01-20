import pandas as pd
import perfplot


def pandas_sum(websites):
    return websites["total_views"].sum()


def loop_sum(websites):
    total = 0
    for row in websites.itertuples():
        total += row.total_views
    return total


def python_sum(websites):
    return sum(row.total_views for row in websites.itertuples())


websites = pd.read_csv("resources/popular_websites.csv", index_col=0)

plot = perfplot.bench(
    n_range=[i**2 for i in range(1, 1000, 100)],
    setup=lambda n: pd.concat([websites for _ in range(n)]),
    kernels=[pandas_sum, loop_sum, python_sum],
    labels=["pandas sum", "loop sum", "python sum"],
)

plot.show()
plot.show(logy=True)
