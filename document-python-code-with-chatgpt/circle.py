"""Prompt
Write NumPy-style docstrings for the following class and its methods:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
"""

import math


# Output:
class Circle:
    """
    A Circle class to perform some circle-related operations.

    Parameters
    ----------
    radius : float
        The radius of the circle.

    Attributes
    ----------
    radius : float
        The radius of the circle.

    Methods
    -------
    calculate_area():
        Calculates the area of the circle.
    """

    def __init__(self, radius):
        """
        Constructs all the necessary attributes for the circle object.

        Parameters
        ----------
        radius : float
            The radius of the circle.
        """
        self.radius = radius

    def calculate_area(self):
        """
        Calculate the area of the circle.

        Returns
        -------
        float
            The area of the circle rounded to 2 decimal places.
        """
        return round(math.pi * self.radius**2, 2)
