from tinydb import TinyDB, where

with TinyDB("ten_countries.json") as countries_db:
    countries_table = countries_db.table(name="countries")

    countries_table.update(
        {"population": 130_575_786}, where("location") == "Mexico"
    )

    countries_table.update(
        {"source": "National quarterly update"},
        where("location") == "Mexico",
    )

# REPL code.
# from pprint import pprint
# from tinydb import TinyDB, where
# with TinyDB("ten_countries.json") as countries_db:
#     countries_table = countries_db.table(name="countries")
#     pprint(countries_table.search(where("location") == "Mexico"))
