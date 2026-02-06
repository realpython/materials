from csv import DictReader

from tinydb import TinyDB

with TinyDB("countries.json", indent=4) as countries_db:
    countries_table = countries_db.table(name="countries")

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
            row["population"] = int(row["population"])
            countries_table.insert(row)
