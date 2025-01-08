# Build Your Personal Diary With Django

This is a companion project to the ["Build Your Personal Diary With Django"](https://realpython.com/django-diary-project-python/) tutorial on Real Python.
Visit the article to follow along or download the content of `source_code_final` folder from this repository.


Type the following commands into a terminal to create and activate a virtual environment and install the requirements:

```sh
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```
Then you can navigate into a step folder, run the database migrations, and create a superuser:

```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```

Finally, run the local Django development server:

```sh
$ python manage.py runserver
```

