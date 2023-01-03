"""
Timing how long it takes to do a complex string replace on a whole column
with various methods
"""

import codetiming
import pandas as pd

# books = pd.read_csv("resources/books.csv")
books = (
    pd.read_csv(
        "https://github.com/realpython/python-data-cleaning/raw/master/Datasets/BL-Flickr-Images-Book.csv"
    )
    .rename(
        columns={
            "Place of Publication": "place_of_publication",
            "Title": "title",
            "Author": "author",
        }
    )
    .loc[:, ["title", "author", "place_of_publication"]]
)

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


def clean_pub_apply(df):
    col = df["place_of_publication"]
    for city in CITIES:
        col = col.apply(lambda val: city if city in val else val)
    return col


def clean_pub_iterrows(df):
    return [
        _replace_city(row["place_of_publication"]) for _, row in df.iterrows()
    ]

    # col = []
    # for _, row in df.iterrows():
    #     place = row["place_of_publication"]
    #     col.append(_replace_city(place))
    # return col


def clean_pub_itertuples(df):
    return [_replace_city(row.place_of_publication) for row in df.itertuples()]

    # col = []
    # for row in df.itertuples():
    #     place = row.place_of_publication
    #     col.append(_replace_city(place))
    # return col


def clean_pub_list_comp(df):
    return [_replace_city(place) for place in df["place_of_publication"]]


for clean_func in [
    clean_pub_replace,
    clean_pub_apply,
    clean_pub_iterrows,
    clean_pub_itertuples,
    clean_pub_list_comp,
]:
    with codetiming.Timer(
        name=clean_func.__name__, text="{name:20}: {milliseconds:.2f} ms"
    ):
        books.assign(place_of_publication=clean_func)
