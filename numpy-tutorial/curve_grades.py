"""Introduction example: curving a series of test grades using Numpy."""

import numpy as np


CURVE_CENTER = 80


def curve(grades):
    """Adjusts an array of grades so that the average is roughly shifted
    to the specified curve center.

    This will never cause a student's grade to decrease, and it will
    never cause the final grade to go over 100%.

    Parameters:
        grades (np.ndarray): The individual student grades, between 0
                             and 100.

    Returns:
        (np.ndarray): A new array of grades, adjusted upwards, but in
                      the same order.
    """
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    return np.clip(new_grades, grades, 100)


if __name__ == "__main__":
    grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
    print(curve(grades))
    # => array([91.25, 54.25, 83.25, 100.0, 70.25, 100.0, 93.25, 31.25])
