# bloggy

A minimal Flask blog in a flat layout. The package's `__init__.py` holds the
application factory, `create_app()`, which registers the `auth` and `posts`
blueprints. Each blueprint has a matching subdirectory under `templates/`.

## Installation

```console
$ python -m pip install -e ".[dev]"
```

## Usage

```console
$ flask --app bloggy init-db
Initialized the database.
$ flask --app bloggy run --debug
```

Then visit `http://127.0.0.1:5000/` and `http://127.0.0.1:5000/auth/login`.
Flask stores the SQLite database in the `instance/` folder, which it creates
next to the package.

## Running the Tests

```console
$ python -m pytest
```
