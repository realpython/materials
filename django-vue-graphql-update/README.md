# Build a Blog Using Django, Vue, and GraphQL

This repository contains code related to the tutorial on [building a blog using Django, Vue, and GraphQL](https://realpython.com/python-django-blog/).

Navigate to the corresponding folder in this repository to compare your code with the code from the tutorial:

- [Step 1](source_code_step_1/)
- [Step 2](source_code_step_2/)
- [Step 3](source_code_step_3/)
- [Step 4](source_code_step_4/)
- [Step 5](source_code_step_5/)
- [Step 6](source_code_step_6/)
- [Step 7](source_code_step_7/)
- [Step 8](source_code_step_8/)
- [Step 9](source_code_final/)

If you want to install the project on your machine without following the tutorial, then you need to follow the steps outlined below.

## Setup

Navigate into the `source_code_final/` folder. In this folder, you'll find the folders `back_end/` and `front_end/`, which represent both projects of the tutorial.

### Back End

Create a new terminal window, navigate into `back_end/`, create, activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), and install the necessary dependencies:

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Then, create the initial Django database by running migrations:

```sh
$ python manage.py migrate
```

Create a Django superuser:

```shell
$ python manage.py createsuperuser
```

Run the Django project:

```sh
$ python manage.py runserver
```

Before continuing, it's a good idea to create some users, profiles, and blog posts in the Django admin interface at `http://localhost:8000/admin`. You must use your superuser credentials to log in.

You can visit the GraphiQL platform `http://localhost:8000/graphql` to try out GraphQL queries.

### Front End

Open a new terminal and navigate into `front_end/`. Then, install the front-end requirements:

```sh
$ npm install --include dev
```

Run the Vite development server:

```sh
$ npm run dev
```

You must have the Django development server and the Vite server running at the same time.
