
```pycon
>>> import sqlite3
>>> conn = sqlite3.connect("people.db")
>>> columns = [
...     "id INTEGER PRIMARY KEY",
...     "lname VARCHAR UNIQUE",
...     "fname VARCHAR",
...     "timestamp DATETIME",
... ]
>>> create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
>>> conn.execute(create_table_cmd)
>>> people = [
...     ("1, 'Fairy', 'Sugar', '2022-10-08 09:15:10'"),
...     ("2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'"),
...     ("3, 'Bunny', 'Easter', '2022-10-08 09:15:27'"),
... ]
>>> for person_data in people:
...     insert_cmd = f"INSERT INTO person VALUES ({person_data})"
...     conn.execute(insert_cmd)
...
>>> conn.commit()
```
