# Bookstore

A small bookstore backend with a REST API, built with FastAPI.

## Endpoints

| Method | Path            | Description                       |
| ------ | --------------- | --------------------------------- |
| `GET`  | `/books`        | List the catalog                  |
| `GET`  | `/books/{isbn}` | Fetch one book                    |
| `POST` | `/quotes`       | Price an order                    |
| `POST` | `/reservations` | Hold copies for an order          |
| `GET`  | `/stock/{isbn}` | Report how many copies are free   |

## Layout

```
.
├── main.py             the FastAPI app and its routes
└── bookstore/
    ├── pricing.py      order pricing
    ├── inventory.py    stock tracking
    ├── catalog.py      book records, read from disk
    └── data/books.json
```

## Running

```console
$ uv sync
$ uv run fastapi dev main.py
```
