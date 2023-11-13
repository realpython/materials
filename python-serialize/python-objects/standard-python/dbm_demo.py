import dbm

with dbm.open("/tmp/cache.db") as db:
    for key in db.keys():
        print(f"{key} = {db[key]}")
