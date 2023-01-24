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


def get_websites(n):
    websites = pd.read_csv("resources/popular_websites.csv", index_col=0)
    if n < len(websites):
        return websites.iloc[:n]
    return pd.concat([websites for _ in range((n // len(websites)) + 1)]).iloc[
        :n
    ]


plot = perfplot.bench(
    n_range=[2**i for i in range(17)],
    setup=get_websites,
    kernels=[pandas_sum, loop_sum, python_sum],
    labels=["pandas sum", "loop sum", "python sum"],
    title="Python vs Pandas sum",
    xlabel="Number of Rows",
)

plot.show()
