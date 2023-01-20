import pandas as pd
from codetiming import Timer


def loop_sum(websites):
    total = 0
    for website in websites.itertuples():
        total += website.total_views
    return total


def python_sum(websites):
    return sum(website.total_views for website in websites.itertuples())


def pandas_sum(websites):
    return websites["total_views"].sum()


for func in [loop_sum, python_sum, pandas_sum]:
    websites = pd.read_csv("resources/popular_websites.csv", index_col=0)
    websites = pd.concat([websites for _ in range(1000)])
    with Timer(name=func.__name__, text="{name:20}: {milliseconds:.2f} ms"):
        func(websites)
