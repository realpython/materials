# greeting.py

"""This module defines some module-level dunder names."""

from __future__ import barry_as_FLUFL

__all__ = ["greet"]
__author__ = "Real Python"
__version__ = "0.1.0"

# import sys


def greet(name="World"):
    print(f"Hello, {name}!")
    print(f"Greetings from version: {__version__}!")
    print(f"Yours, {__author__}!")
