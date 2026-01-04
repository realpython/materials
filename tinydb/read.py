from pprint import pprint
from tinydb import Query, TinyDB

countries_db = TinyDB("ten_countries.json")
countries_tb = countries_db.table(name="countries")

query = Query()
query_def = (query.population > 220_000_000) & (
    query.population < 250_000_000
)

pprint(countries_tb.search(query_def))

pprint(countries_tb.search(query["% of world"] >= 17))
