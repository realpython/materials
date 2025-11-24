# How to Create a Django Project

Follow tutorial on [How to Create a Django Project](https://realpython.com/django-setup/) on Real Python to create a new Django project with one Django app from scratch.

> **Note:** This project targets Python 3.10 or later.

## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
$ python3 -m venv venv
```

Activate the virtual environment:

```bash
$ source venv/bin/activate
```

Install the dependencies for this project:

```bash
(venv) $ python -m pip install -r requirements.txt
```

## Run the Scaffold

Navigate into the Django project folder:

```bash
(venv) $ cd setup
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/` to see the starter project in action.
