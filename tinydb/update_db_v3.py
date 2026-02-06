from tinydb import TinyDB

with TinyDB("ten_countries.json") as countries_db:
    countries_table = countries_db.table(name="countries")
    countries_table.update({"source": "Official estimate"}, doc_ids=[7, 9])
