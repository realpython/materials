# Get Started With Django Part 3: Django View Authorization, Code Examples

This folder contains the sample code for [Get Started With Django Part 3: Django View Authorization](https://realpython.com/django-view-authorization/).

The code was tested with Python 3.8 and Django 3.0.7. To install the same version, use:

    python -m pip install -r requirements.txt

This tutorial uses the Django admin, and comes with some sample data. To get going you will need to run the following commands:

    cd Blog
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py loaddata core.json

Once those commands are complete, you can run the Django development server:

    python manage.py runserver

With the server running, visit `http://127.0.0.1:8000` in your web browser to see the results.
