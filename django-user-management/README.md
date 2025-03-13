# Get Started With Django User Management

Follow the [step-by-step instructions](https://realpython.com/django-user-management/) on Real Python.

## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
$ python3 -m venv venv/
```

Activate the virtual environment:

```bash
$ source venv/bin/activate
```

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
```

Navigate into the project's directory:

```bash
(venv) $ cd user_auth_intro/
```

Make and apply the migrations for the project to build your local database:

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/dashboard` to see the project in action.
