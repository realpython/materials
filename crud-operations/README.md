# What Are CRUD Operations?

This repository contains code related to the Real Python tutorial on [building a front end for a REST API](https://realpython.com/crud-operations/).

## Setup

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

Then you can execute `crud_sql_alchemy.py` to create a new database:

```sh
(venv) $ python crud_sql_alchemy.py
```

This will create a `birds.db` database that you can use to try out CRUD operations.

## Examples

Start a new [Python REPL](https://realpython.com/python-repl/) to perform CRUD operations with raw SQL:

```pycon
>>> from crud_sql import connect_to_db
>>> connection = connect_to_db("birds.db")
>>> create_birds = """
... INSERT INTO
...   bird (name)
... VALUES
...   ('Hummingbird'),
...   ('Sugar Glider');
... """
>>> connection.execute(create_birds)
<sqlite3.Cursor object at 0x105027bc0>

>>> connection.commit()
>>> connection.close()
```

You can also use SQL Alchemy to interact with the database:

```pycon
>>> from crud_sql_alchemy import Session, Bird, init_db
>>> init_db()
>>> session = Session()
>>> new_bird = Bird(name="Test Bird")
>>> session.add(new_bird)
>>> session.commit()
```

If you're curious to explore CRUD operations with a REST API, then you can run this command in the terminal:

```console
(venv) $ uvicorn crud_fastapi:app
```

Once the server is running, you can test out the Rest API endpoints by visiting `http://127.0.0.1:8000/docs` in your browser.

## Author

- **Philipp Acsany**, E-mail: [philipp@realpython.com](philipp@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
