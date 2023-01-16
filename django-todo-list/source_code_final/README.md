# Django Todo List

This folder contains project code for the _Real Python_ step-by-step project for building a to-do app with Django.

## Setup Instructions

These instructions have been tested in Ubuntu Linux and macOS. They should also work in Windows, but note that you'll need to use a different command to activate your virtual environment as described in Step 3. Please consult the [`venv` documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for greater detail on the use of virtual environments.

1. Navigate into the project directory (`source_code/`).
2. Create a virtual environment in a `venv/` folder by typing `python -m venv venv` in your console.
3. Activate the venv using `source venv/bin/activate` (Linux, MacOS) or `venv\Scripts\activate.bat` (Windows).
4. Install the dependencies with `python -m pip install -r requirements.txt`
5. Generate the empty SQLite database and tables using `python manage.py migrate`
5. Run the app with `python manage.py runserver`
6. Browse to the [app home page](http://localhost:8000/) to see the list of todo lists, which will initially be empty. 

You can now start using the UI to add your to-do lists and to-do items to the database. The data will be stored in a new `db.sqlite3` file in the root of your project directory.

You can also use Django's auto-generated [admin interface](https://realpython.com/customize-django-admin-python/#setting-up-the-django-admin) at `http://localhost:8000/admin/` to view, add, and edit the data.
