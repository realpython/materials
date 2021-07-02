# Django Diary

> **Note:** The project is built with `Python 3.9.1`, but should work with any Python3 version.

## About this repository

This is a companion project to the ["Build Your Personal Diary With Django"](https://realpython.com/build-a-django-diary) tutorial on Real Python.
Visit the article to follow along or download the content of `source_code_final` folder from this repository.

## How To Run `django-diary`

Type the following commands into a terminal to create and activate a virtual environment and install the requirements:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```

Then run the database migrations and create a superuser:

```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```

Finally, run the local Django development server:

```sh
$ python manage.py runserver
```

## License

Distributed under the MIT license.
