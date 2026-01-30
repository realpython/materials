from csv import DictReader
from pprint import pprint

from tinydb import TinyDB

with TinyDB("countries.json", indent=4) as countries:
    countries_table = countries.table(name="countries")

    countries_table.insert({"location": "Vatican City", "population": 501})

    countries_table.insert_multiple(
        [
            {"location": "India", "population": 1_417_492_000},
            {"location": "China", "population": 1_408_280_000},
        ]
    )

    with open("countries_file.csv", "r") as csv_source:
        reader = DictReader(csv_source)

        for row in reader:
            countries_table.insert(row)

    pprint(countries_table.get(doc_ids=[3, 4]))
