# Python Project Structure: How to Choose the Right Layout

This folder provides the code examples for the Real Python tutorial [Python Project Structure: How to Choose the Right Layout](https://realpython.com/python-application-layouts/).

Each subfolder turns one of the tutorial's example directory trees into a small, working project that you can open, install, and run:

| Folder       | Project Type    | Layout | Try It                                                 |
|--------------|-----------------|--------|--------------------------------------------------------|
| `statkit/`   | Library         | `src/` | `python -m pytest`                                     |
| `weatherly/` | CLI application | Flat   | `weatherly lisbon` or `python -m weatherly lisbon`     |
| `portfolio/` | Django project  | Flat   | `python manage.py runserver`                           |
| `bloggy/`    | Flask project   | Flat   | `flask --app bloggy run`                               |
| `bookapi/`   | FastAPI project | Flat   | `uvicorn bookapi.main:app`                             |
| `notely/`    | GUI application | Flat   | `notely` or `python -m notely`                         |

The projects are minimal skeletons. They contain just enough code to make each tree real, and each one has its own `README.md` with details.

## Installation

The projects don't share a top-level `requirements.txt`. Instead, each project declares its own pinned dependencies in its `pyproject.toml`, just like a standalone repository would. Create a separate virtual environment for each project, change into its folder, and install it in editable mode along with its test dependencies:

```console
$ cd statkit/
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -e ".[dev]"
(venv) $ python -m pytest
```

The same steps work for `weatherly/`, `bloggy/`, `bookapi/`, and `notely/`. The Django `portfolio/` project isn't meant to be installed, so you only install Django there:

```console
(venv) $ python -m pip install django==6.1.2
(venv) $ python manage.py check
```

## Notes

- The `weatherly` CLI doesn't call any real weather API. Its only provider returns canned data, so it works offline.
- Folders that would otherwise be empty, such as `portfolio/static/` and `notely/notely/resources/translations/`, contain a `.gitkeep` file so that Git keeps them.
- The tests in `notely/` use Qt's `offscreen` platform, so they don't open any windows.

The code requires Python 3.10 or later, and the Django project requires Python 3.12 or later because of Django 6.1.
