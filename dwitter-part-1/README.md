# Dwitter - Your tiny social network built with Django

This web app models the basic functionality of Twitter.

You can:

- **post** short text messages
- **view** all users on the platform
- **follow** and unfollow other users
- **inspect** a feed of messages from users that you follow

Follow the step-by-step instructions of the associated _Real Python_ tutorial to build your own version of Dwitter.

## Setup

You can run the provided example project on your local machine by following the steps outlined below.

Create a new virtual environment:

```bash
python3 -m venv ./venv
```

Activate the virtual environment:

```bash
source ./venv/bin/activate
```

Install the dependencies for this project:

```bash
(venv) $ python -m pip install -r requirements.txt
```

Make and apply the migrations for the project to build your local database:

```bash
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

Create a superuser that allows you to log in to your Django admin portal:

```bash
(venv) $ python manage.py createsuperuser
```

Run the Django development server:

```bash
(venv) $ python manage.py runserver
```

Navigate to `http://localhost:8000/admin` and log in with your superuser credentials. You can create users through the Django admin and explore your social media platform with multiple users.
