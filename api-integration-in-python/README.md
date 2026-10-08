# Python and REST APIs: Interacting With Web Services

This folder provides the code examples for the Real Python tutorial [Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python/).

The examples are grouped into one subfolder per section of the tutorial, because the Flask and FastAPI examples both use a file called `app.py`, and because the tutorial itself advises you to keep each example in its own folder:

- `consuming-apis/`: the `requests` examples from **REST and Python: Consuming APIs**. The tutorial shows these in the REPL, so here they're runnable scripts that `print()` the results, one script per HTTP method section.
- `flask-api/`: the Flask countries API from **Tools of the Trade → Flask**.
- `django-api/`: the `countryapi` Django project with Django REST framework from **Tools of the Trade → Django REST Framework**.
- `fastapi-api/`: the FastAPI countries API from **Tools of the Trade → FastAPI**.

## Setup

Create and activate a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies:

```console
(venv) $ python -m pip install -r requirements.txt
```

The single `requirements.txt` covers all four examples. If you'd rather isolate them, then create one virtual environment per subfolder and install only the packages that example needs.

## Consuming APIs With `requests`

Each script sends one kind of request to [JSONPlaceholder](https://jsonplaceholder.typicode.com/) and prints the response, so you need an internet connection to run them:

```console
(venv) $ cd consuming-apis/
(venv) $ python get_request.py
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
200
application/json; charset=utf-8
```

The other scripts are `post_request.py`, `put_request.py`, `patch_request.py`, and `delete_request.py`.

## Flask

```console
(venv) $ cd flask-api/
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_DEBUG=1
(venv) $ flask run
```

Then request the endpoint at `http://127.0.0.1:5000/countries`.

## Django REST Framework

The `django-api/` folder is the `countryapi` project that the tutorial creates with `django-admin startproject countryapi` and `python manage.py startapp countries`. Set up its database and load the fixture before you start the server:

```console
(venv) $ cd django-api/
(venv) $ python manage.py migrate
(venv) $ python manage.py loaddata countries.json
Installed 3 object(s) from 1 fixture(s)
(venv) $ python manage.py runserver
```

Then request the endpoint at `http://127.0.0.1:8000/countries/`.

## FastAPI

```console
(venv) $ cd fastapi-api/
(venv) $ uvicorn app:app --reload
```

Then request the endpoint at `http://127.0.0.1:8000/countries`.
