# notely

A minimal desktop notes app built with PySide6 in a flat layout, split along
the Model-View-Controller (MVC) pattern:

- `models/`: The `Note` data class and a `NoteStore` that persists notes to a
  JSON file in your home folder
- `views/`: The `MainWindow`, which loads its widgets from the Qt Designer file
  `views/ui/main_window.ui`
- `controllers/`: The `NoteController`, which handles input and keeps the view
  and the model in sync
- `resources/`: The app icon and an empty `translations/` folder

The app loads the `.ui` file and the icon with `importlib.resources`, and
the `[tool.setuptools.package-data]` table in `pyproject.toml` makes sure
both ship with the package.

## Installation

```console
$ python -m pip install -e ".[dev]"
```

## Usage

```console
$ notely
```

You can also run `python -m notely`.

## Running the Tests

The tests use Qt's `offscreen` platform, so they don't open any windows:

```console
$ python -m pytest
```
