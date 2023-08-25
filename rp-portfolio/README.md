# Get Started With Django: Build a Portfolio App

Follow the [step-by-step instructions](https://realpython.com/get-started-with-django-1/) on Real Python to build your own portfolio project with Django.

## Images

You can find the example images for the projects in the [uploads/project_images](uploads/project_images) folder.

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

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
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

Navigate to `http://localhost:8000/` or `http://localhost:8000/projects` to see your portfolio project in action.
