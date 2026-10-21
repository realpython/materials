# ruff: noqa: F401
"""Illustration of good import statement styling.

Note that the imports come after the docstring.

"""

# Standard library imports
import datetime
import os

# Third party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Local application imports
from local_module import local_class
from local_package import local_function
