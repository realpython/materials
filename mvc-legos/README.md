# Model-View-Controller (MVC) in Python Web Apps: Explained With Legos

This folder contains a minimal Flask example app that supports the explanation of the MVC pattern in [Model-View-Controller (MVC) Explained – With Legos](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/).

To run the app, you'll need to first install [Flask](https://flask.palletsprojects.com/), preferably into a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```sh
(venv) $ python -m pip install Flask
```

To create and see the SQLite database file, you can then run `create_db.py`:

```sh
(venv) $ python create_db.py
```

Finally, you can start the Flask app by executing `app.py`:

```sh
(venv) $ python app.py
```

When you make a request in your browser by typing the URL of your localhost and port 8000, you'll see how Flask renders the single view that this web app defines.
