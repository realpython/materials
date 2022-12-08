# Build a Frontend for a REST API

This repository contains code related to the tutorial on [building a frontend for a REST API](https://realpython.com/build-a-rest-api-frontend/).

## Setup

You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

Then you can navigate into the folder `source_code_start/` and create a new database:

```sh
(venv) $ cd source_code_start
(venv) $ python build_database.py
```

This will delete any existing database and create a new database named `people.db` that you can use with your project.

After building the database, you can start the Flask server:

```sh
(venv) $ python app.py
```

When the Flask server is running, you can visit the frontend on `http://localhost:8000` and the API documentation on `http://localhost:8000/api/ui`.

## Author

- **Philipp Acsany**, E-mail: [philipp@realpython.com](philipp@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
