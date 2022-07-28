# calculations3.py

"""This module implements custom calculations."""

# Imports go here...
from configparser import ConfigParser

# import numpy as np

constants = ConfigParser()
constants.read("path/to/constants.ini")


# Your custom calculations start here...
def circular_land_area(radius):
    return float(constants.get("CONSTANTS", "PI")) * radius**2


def future_value(present_value, interest_rate, years):
    return (
        present_value * float(constants.get("CONSTANTS", "EULER_NUMBER"))
    ) ** (interest_rate * years)


# ...
