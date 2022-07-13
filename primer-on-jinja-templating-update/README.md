# Primer on Jinja Templating

This repository holds the code for the Real Python [Primer on Jinja Templating](https://realpython.com/primer-on-jinja-templating/) tutorial.

## Dependencies

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

You can then install Jinja and Flask with `pip`:

```console
(venv) $ python -m pip install Jinja2 flask
```

Alternatively, you can install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

This command will install the versions used in the tutorial of Jinja, Flask, and their dependencies.

## Run the Web App

You can start your Flask development server by running `app.py` as a script:

```console
(venv) $ python app.py
```

To see your home page, visit `http://127.0.0.1:5000`.

## Author

- **Philipp Acsany**, E-mail: [philipp@realpython.com](philipp@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
