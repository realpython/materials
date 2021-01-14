# RP Contacts

**RP Contacts** is a Contact Book application built with Python, [PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html), and [SQLite](https://www.sqlite.org/docs.html).

## Running the Application

To run **RP Contacts**, you need to download the sorce code. Then open a terminal or command-line window and run the following steps:

1. Create and activate a Python virtual environment

```sh
$ cd rpcontacts/
$ python3 -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the dependencies

```sh
(venv) $ pip install -r requirements.txt
```

3. Run the application

```sh
(venv) $ python3 rpcontacts.py
```

**Note:** This application was built using Python 3.8.5 and PyQt 5.15.1.

## Sample Data

If you want to add some sample data to **RP Contacts** to test the application, then run the following command:

```sh
(venv) $ python3 sample_data.py
```

## Release History

- 0.1.0
  - A work in progress

## About the Author

Leodanis Pozo Ramos – [@lpozo78](https://twitter.com/lpozo78) – leodanis@realpython.com

## License

Distributed under the MIT license.
