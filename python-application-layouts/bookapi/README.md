# bookapi

A minimal book-catalog API built with FastAPI in a flat layout, following the
shape of FastAPI's bigger-applications tutorial. `main.py` builds the app and
includes the routers from `routers/` and the admin-only router from
`internal/`. The "database" in `dependencies.py` is an in-memory dictionary.

## Installation

```console
$ python -m pip install -e ".[dev]"
```

## Usage

There's no `__main__.py`. Instead, point an ASGI server at `bookapi.main:app`:

```console
$ uvicorn bookapi.main:app --reload
```

Then try the endpoints:

```console
$ curl http://127.0.0.1:8000/books/1
{"id":1,"title":"A Wizard of Earthsea","author_id":1}
$ curl -X POST -H "X-Token: fake-super-secret-token" http://127.0.0.1:8000/admin/
{"message":"Catalog updated"}
```

You can also explore the interactive docs at `http://127.0.0.1:8000/docs`.

## Running the Tests

```console
$ python -m pytest
```
