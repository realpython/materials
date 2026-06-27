# Django Tasks: Exploring the Built-in Tasks Framework

Example project for the Real Python tutorial [Django Tasks: Exploring the Built-in Tasks Framework](https://realpython.com/django-tasks/).

The project demonstrates Django 6's `@task` decorator, the `django-tasks-db` database-backed worker, named queues with priorities, and the `transaction.on_commit` pattern for safe enqueueing inside an atomic block.

## Setup

Set up a virtual environment and install dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Run migrations:

```sh
(venv) $ python -m manage makemigrations myapp
(venv) $ python -m manage migrate
```

## Run

The project uses two processes: the Django dev server and the `db_worker`.

In one terminal, start the worker:

```sh
(venv) $ python -m manage db_worker --queue-name '*'
```

In a second terminal, start the dev server:

```sh
(venv) $ python -m manage runserver
```

Trigger the demo endpoints with `curl` or your browser:

```sh
$ curl 'http://localhost:8000/register/?email=alice@example.com&name=Alice'
$ curl http://localhost:8000/checkout/
$ curl http://localhost:8000/task-status/<task-id>/
```

You can also enqueue tasks from the Django shell:

```sh
(venv) $ python -m manage shell
```

```pycon
>>> from myapp.tasks import say_hello
>>> result = say_hello.enqueue("Real Python")
>>> result.refresh()
>>> result.status
SUCCESSFUL
>>> result.return_value
'Hello, Real Python!'
```
