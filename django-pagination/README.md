# Pagination for a User-Friendly Django App

This repository contains the source code for the Django project that you'll complete in Real Python's [Pagination for a User-Friendly Django App](https://realpython.com/django-pagination/).

## Create the Django Project

After you've cloned this repository and navigated into its folder, you can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
$ python3 -m venv venv
```

Activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Navigate to the folder for the step that you're currently on.

Install the dependencies for this project if you haven't installed them yet:

```bash
(venv) $ python -m pip install -r requirements.txt
```

Apply the migrations for the project to build your local database:

```bash
(venv) $ python manage.py migrate
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/all`.
You should see an empty page with a _Python Keywords_ headline.

## Prepare the Database

Run the Django migrations:

```bash
(venv) $ python manage.py migrate
```

This will create the tables for the Python wiki project in your database.

## Add the Python Keywords Data

Enter the Django shell:

```bash
(venv) $ python manage.py shell
````

Add the Python keywords to your database:

```pycon
>>> import keyword
>>> from terms.models import Keyword
>>> for kw in keyword.kwlist:
...     k = Keyword(name=kw)
...     k.save()
...
```

Verify that the keywords were added to your database:

```pycon
Keyword.objects.all()
>>> Keyword.objects.all()
<QuerySet [<Keyword: False>, <Keyword: None>, <Keyword: True>, <Keyword: and>, <Keyword: as>, <Keyword: assert>, <Keyword: async>, <Keyword: await>, <Keyword: break>, <Keyword: class>, <Keyword: continue>, <Keyword: def>, <Keyword: del>, <Keyword: elif>, <Keyword: else>, <Keyword: except>, <Keyword: finally>, <Keyword: for>, <Keyword: from>, <Keyword: global>, '...(remaining elements truncated)...']>
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/all` to see the page with all the Python keywords.
