# Hosting a Django Project on Heroku

This is a companion project to a Real Python tutorial about [hosting a Django project on Heroku](https://realpython.com/django-hosting-on-heroku/). It's a bare-bones Django project without any views.

## Instructions

You should follow the step-by-step instructions in the tutorial to deploy this project to Heroku. Alternatively, you can run the finished project by following the instructions below.

Download the code by cloning the `materials` repository:

```shell
$ git clone https://github.com/realpython/materials.git
```

Create a new local Git repository:

```shell
$ cd materials/django-hosting-heroku/source_code_final/portfolio-project
$ git init
$ git add .
$ git commit -m "Initial commit"
```

Deploy the code to Heroku:

```shell
$ heroku login
$ heroku create
$ heroku config:set DEBUG=True SECRET_KEY=$(head -c 32 /dev/urandom | base64)
$ git push heroku master
$ heroku open
```

Optionally, for local development:

```shell
$ python3 -m venv ./venv --prompt portfolio
$ source venv/bin/activate
(portfolio) $ python -m pip install -r requirements.txt
(portfolio) $ python -m pip install --upgrade pip
(portfolio) $ heroku config --shell > .env
(portfolio) $ heroku local
```

Navigate your web browser to <http://0.0.0.0:5000/>

**Note:** If you're on a Mac, then you may run into issues with the `heroku local` command above. To mitigate it, try commenting out the line with your `DATABASE_URL` variable from the `.env` file. Alternatively, you can uninstall the `psycopg2` driver and install its binary counterpart:

```console
$ pip uninstall psycopg2
$ pip install psycopg2-binary
```
