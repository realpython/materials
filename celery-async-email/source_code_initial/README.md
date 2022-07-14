# Asynchronous Tasks with Django and Celery

Example project for tutorial update.

## Setup (macOS)

To try the project, set up a virtual environment and install the listed dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

You'll also need to install Redis on your system:

```sh
brew install redis
```

Once you've installed all the dependencies, you need to start three processes that need to run at the same time:

1. Django
2. Redis
3. Celery

To get all of them running, open three different terminal windows and start them one-by-one:

**Django app:**

```sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

**Redis server:**

```sh
(venv) $ redis-server
```

**Celery:**

```sh
(venv) $ python -m celery -A django_celery worker -l info
```

When all three processes are running, you can head over to `localhost:8000/feedback` and submit a feedback response. Celery will simulate a work-intensive process and send an email at the end of it. You'll see the email message show up in the log stream on the terminal window where the Celery worker is running.
