# Build a Frontend for a REST API

This repository contains code related to the tutorial on [building a frontend for a REST API](https://realpython.com/build-a-rest-api-frontend/).

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), then install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Then you can navigate into the folder `source_code_final/` and create a new database:

```sh
(venv) $ cd source_code_final
(venv) $ python build_databas.py
```

After building the database, you can start the Flask server:

```sh
(venv) $ python app.py
```

When the Flask server is running, you can visit the frontend on `http://localhost:8000` and the API documentation on `http://localhost:8000/api/ui`.
