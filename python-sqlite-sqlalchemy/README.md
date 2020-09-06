# Python / SQLite /SQLAlchemy article

This repository contains the content and example code
for the Python / SQLite / SQLAlchemy article I'm writing
for Real Python.

This project was built using Python 3.8.0

## Python Virtualenv

I use the `pyenv` tool to install Python versions on my Mac. I find it a very useful tool, and the instructions that follow use it, and are based on having Python version 3.8.0 installed using the following command:

```shell
$ pyenv install 3.8.0
```

## Installing The Project

From the main folder take the following steps (on a Mac):

* Install a Python virtual environment for this project
  * `pyenv local 3.8.0`
  * `python -m venv .venv`
* Activate the virtual environment
  * `source .venv/bin/activate`
* Install the project:
  * `python -m pip install -e .`
