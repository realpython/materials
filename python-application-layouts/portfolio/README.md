# portfolio

A minimal Django project for a personal portfolio site in a flat layout. The
`portfolio/` package comes from `django-admin startproject`, and the
`blog`, `contact`, and `projects` apps live under `apps/`. Because of that,
each app's `AppConfig.name` and `INSTALLED_APPS` entry use the full dotted
path, such as `"apps.blog"`.

## Installation

```console
$ python -m pip install django==6.1.2
```

The same pinned dependency appears in `pyproject.toml`, which this project
uses for metadata only. You run a Django project through `manage.py`, so
there's no need to install the project itself.

## Usage

```console
$ python manage.py check
$ python manage.py runserver
```

Then visit `http://localhost:8000/`, `/blog/`, and `/contact/`.

## Running the Tests

```console
$ python manage.py test
```
