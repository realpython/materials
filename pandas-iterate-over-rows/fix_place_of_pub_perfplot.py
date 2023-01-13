"""
Plotting how long it takes to do a complex string replace on a whole column
with various methods.

In the dataset, in the `place_of_publication` column, you've got entries like
these:

London
London; Virtue & Yorston
Oxford
pp. 40. G. Bryan & Co: Oxford, 1898
Plymouth
pp. 40. W. Cann: Plymouth, [1876?]

Most of these are just city names, but some have additional and unwanted
information. For these, you want to detect if it has one of the city names,
replacing the whole value with just the city name.
"""

import pandas as pd
import perfplot

books = pd.read_csv("resources/books.csv")

CITIES = ["London", "Plymouth", "Oxford", "Boston"]


def _replace_city(text):
    for city in CITIES:
        if city in text:
            return city
    return text


def clean_pub_replace(df):
    col = df["place_of_publication"]
    for city in CITIES:
        col = col.replace(rf".*{city}.*", city, regex=True)
    return col


def clean_pub_itertuples(df):
    return [_replace_city(row.place_of_publication) for row in df.itertuples()]


def clean_pub_iterrows(df):
    return [
        _replace_city(row["place_of_publication"]) for _, row in df.iterrows()
    ]


def clean_pub_apply(df):
    col = df["place_of_publication"]
    for city in CITIES:
        col = col.apply(lambda val: city if city in val else val)
    return col


def clean_pub_list_comp(df):
    return [_replace_city(place) for place in df["place_of_publication"]]


def get_books(n):
    books = pd.read_csv("resources/books.csv")
    if n < len(books):
        return books.iloc[:n]
    return pd.concat([books for _ in range((n // len(books)) + 1)]).iloc[:n]


plot = perfplot.bench(
    setup=lambda n: get_books(n),
    kernels=[
        clean_pub_replace,
        clean_pub_itertuples,
        clean_pub_iterrows,
        clean_pub_apply,
        clean_pub_list_comp,
    ],
    labels=["replace", "itertuples", "iterrows", "apply", "list comp"],
    n_range=[i**2 for i in range(1, 40, 2)],
    equality_check=None,
)

plot.show()
plot.show(logy=True)
