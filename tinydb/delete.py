from tinydb import TinyDB, where

countries_db = TinyDB("ten_countries.json")
countries_tb = countries_db.table(name="countries")

len(countries_tb)

countries_tb.remove(doc_ids=[3, 5, 7])

len(countries_tb)

countries_tb.remove(where("population") < 300_000_000)

countries_tb.truncate()
len(countries_tb)

countries_db.tables()

countries_db.drop_table(name="countries")

countries_db.tables()
