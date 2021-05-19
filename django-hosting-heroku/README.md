# How to Host Your Django Project on Heroku

This is a companion project to a tutorial on Real Python. It's a bare-bones Django project without any views.

## Instructions

You should follow the step-by-step instructions in the tutorial to deploy this project to Heroku. Alternatively, you can run the finished project by following the instructions below.

Download the code by cloning the `materials` repository:

```shell
$ git clone git@github.com:realpython/materials.git
```

Create a new local Git repository:

```shell
$ cd materials/django-hosting-heroku
$ git init
$ git add .
$ git commit -m "Initial commit"
```

Deploy the code to Heroku:

```shell
$ heroku login
$ heroku create
$ heroku config:set DEBUG=True SECRET_KEY=$(date | base64)
$ git push heroku master
$ heroku open
```

Optionally, for local development:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ heroku config -s > .env
$ heroku local
```

Navigate your web browser to <http://0.0.0.0:5000/>
