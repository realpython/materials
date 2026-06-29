# Qt Designer and Python: Build Your GUI Applications Faster

This folder provides the code examples for the Real Python tutorial [Qt Designer and Python: Build Your GUI Applications Faster](https://realpython.com/qt-designer-python/)

## How to Run This Application

Create and activate a Python virtual environment, then install [PyQt6](https://pypi.org/project/PyQt6/):

```sh
$ python3 -m venv ./venv
$ source venv/bin/activate
(venv) $ python -m pip install pyqt6
```

Then launch the sample text editor from the `sample_editor/` directory:

```sh
(venv) $ cd sample_editor/
(venv) $ python app.py
```

Run `app.py` from inside `sample_editor/`, because the application loads its `.ui` files and icons through relative paths.

## License

The icons used in this application are part of the [TurkinOS](https://github.com/llamaret/turkinos-icon) icon theme, distributed under the [GPL v3.0 license](https://github.com/llamaret/turkinos-icon/blob/master/LICENSE). See `ui/resources/LICENSE` for details.
