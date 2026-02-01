# REPL code

from tinydb import TinyDB, where

countries_db = TinyDB("ten_countries.json")
countries_table = countries_db.table(name="countries")
len(countries_table)

countries_table.remove(doc_ids=[3, 5, 7])

len(countries_table)

countries_table.remove(where("population") < 300_000_000)
len(countries_table)

countries_table.truncate()
len(countries_table)

countries_db.tables()

countries_db.drop_table(name="countries")
countries_db.tables()
