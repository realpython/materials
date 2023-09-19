# calculations.py

"""This module implements custom calculations."""

# Imports go here...
# import numpy as np

from . import constants


# Your custom calculations start here...
def circular_land_area(radius):
    return constants.PI * radius**2


def future_value(present_value, interest_rate, years):
    return present_value * constants.EULER_NUMBER ** (interest_rate * years)
