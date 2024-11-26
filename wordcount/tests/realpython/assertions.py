"""PYTEST_DONT_REWRITE"""  # Disable pytest's assertion rewriting for this module!

from .exceptions import RealPythonAssertionError


def assert_equals(expected, actual, message=None):
    if expected != actual:
        raise RealPythonAssertionError(expected, actual, message)


def assert_equals_if(expected, actual, message=None):
    """Only show the expected vs. actual table on a truthy value."""
    if bool(actual):
        assert_equals(expected, actual, message)
    else:
        if message:
            assert expected == actual, message
        else:
            assert expected == actual
