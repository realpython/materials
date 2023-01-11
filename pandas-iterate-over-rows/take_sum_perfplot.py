import pandas as pd
import perfplot


def pandas_sum(df):
    return df["total_views"].sum()


def loop_sum(df):
    total = 0
    for row in df.itertuples():
        total += row.total_views
    return total


def python_sum(webs):
    return sum(row.total_views for row in webs.itertuples())


webs = pd.read_csv("resources/popular_websites.csv", index_col=0)

perfplot.live(
    n_range=[i**2 for i in range(1, 1000, 100)],
    setup=lambda n: pd.concat([webs for _ in range(n)]),
    kernels=[pandas_sum, loop_sum, python_sum],
    labels=["pandas sum", "loop sum", "python sum"],
    # equality_check=None,
    logy=True,
)
