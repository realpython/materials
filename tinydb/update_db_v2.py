from tinydb import TinyDB, where

with TinyDB("ten_countries.json") as countries_db:
    countries_table = countries_db.table(name="countries")
    countries_table.update_multiple(
        [
            (
                {"population": 130_575_786},
                where("location") == "Mexico",
            ),
            (
                {"source": "National quarterly update"},
                where("location") == "Mexico",
            ),
        ]
    )
