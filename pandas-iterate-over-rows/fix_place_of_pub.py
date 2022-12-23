"""
Timing how long it takes to do a complex string replace on a whole column
with various methods
"""

import codetiming
import pandas as pd

books = pd.read_csv("resources/books.csv")

CITIES = ["London", "Plymouth", "Oxford", "Boston"]


def clean_pub_replace(df):
    def clean_pub_replace_inner(df):
        col = df["place_of_publication"]
        for city in CITIES:
            col.replace(rf".*{city}.*", city, regex=True)
        return col

    return df.assign(place_of_publication=clean_pub_replace_inner)


def clean_pub_apply(df):
    def clean_pub_apply_inner(df):
        col = df["place_of_publication"]
        for city in CITIES:
            col = col.apply(lambda val: city if city in val else val)
        return col

    return df.assign(place_of_publication=clean_pub_apply_inner)


def clean_pub_iterrows(df):
    def clean_pub_iterrows_inner(df):
        col = []
        for _, row in df.iterrows():
            place = row["place_of_publication"]

            for name in CITIES:
                place = name if name in place else place

            col.append(place)

        return col

    return df.assign(place_of_publication=clean_pub_iterrows_inner)


def clean_pub_itertuples(df):
    def clean_pub_itertuples_inner(df):
        col = []
        for row in df.itertuples():
            place = row.place_of_publication
            for name in CITIES:
                place = name if name in place else place

        col.append(place)

    return df.assign(place_of_publication=clean_pub_itertuples_inner)


def clean_pub_list_comp(df):
    def replace_city(text):
        for city in CITIES:
            if city in text:
                return city

        return text

    def clean_pub_list_comp_inner(df):
        return [replace_city(place) for place in df["place_of_publication"]]

    return df.assign(place_of_publication=clean_pub_list_comp_inner)


for f in [
    clean_pub_apply,
    clean_pub_iterrows,
    clean_pub_itertuples,
    clean_pub_replace,
    clean_pub_list_comp,
]:
    with codetiming.Timer(
        name=f.__name__, text="{name:20}: {milliseconds:.2f} ms"
    ):
        f(books)
