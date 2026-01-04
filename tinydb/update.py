from pprint import pprint
from tinydb import TinyDB, where

with TinyDB("ten_countries.json") as countries_db:
    countries_tb = countries_db.table(name="countries")
    countries_tb.update(
        {"population": 130_575_786}, where("location") == "Mexico"
    )
    countries_tb.update(
        {"source": "National quarterly update"},
        where("location") == "Mexico",
    )
    pprint(countries_tb.search(where("location") == "Mexico"))

    countries_tb.update_multiple(
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

    countries_tb.update(
        {"source": "Official estimate"}, doc_ids=[7, 9]
    )
