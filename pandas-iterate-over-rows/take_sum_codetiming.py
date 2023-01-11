import codetiming
import pandas as pd


def pandas_sum(webs):
    return webs["total_views"].sum()


def loop_sum(webs):
    total = 0
    for row in webs.itertuples():
        total += row.total_views
    return total


def python_sum(webs):
    return sum(row.total_views for row in webs.itertuples())


for f in [pandas_sum, loop_sum, python_sum]:
    webs = pd.read_csv("resources/popular_websites.csv", index_col=0)
    with codetiming.Timer(
        name=f.__name__, text="{name:20}: {milliseconds:.2f} ms"
    ):
        f(webs)
