# Model-View-Controller (MVC) in Python Web Apps: Explained With Legos

This folder contains a minimal Flask example app that supports the explanation of the MVC pattern in [Model-View-Controller (MVC) Explained – With Lego](https://realpython.com/lego-model-view-controller-python/).

To run the app, you'll need to first install [Flask](https://flask.palletsprojects.com/), preferably into a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```sh
(venv) $ python -m pip install Flask
```

Then, you can start the Flask app by executing `app.py`:

```sh
(venv) $ python app.py
```

When you make a request in your browser by typing the URL of your localhost and port 8000, you'll see how Flask renders the single view that this web app defines.

---

**Note:** The SQLite database file was created by running `create_db.py`. You can modify this file to change the content in the database. Then run the script to update the database:

```sh
(venv) $ python create_db.py
```

