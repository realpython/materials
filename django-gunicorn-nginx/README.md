# Securely Deploy a Django App With Gunicorn, Nginx, & HTTPS

This directory contains the Django project created in the tutorial [Securely Deploy a Django App With Gunicorn, Nginx, & HTTPS](https://realpython.com/django-nginx-gunicorn/).

It requires Python 3.8 or higher and Django 3.2.

Here's what this repository and the tutorial illustrate:

- How you can take your Django app **from development to production**
- How you can **host your app** on a real-world public domain
- How to introduce **Gunicorn** and **Nginx** into the request and response chain
- How **HTTP headers** can fortify your site's HTTPS security

To get started, install requirements and migrate your database:

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements/prod.txt
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
python3 manage.py migrate
python3 manage.py check
```
