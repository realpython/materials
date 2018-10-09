"""Examples of decorators that work with Flask

See  https://realpython.com/primer-on-python-decorators/

These decorators depend on the third party package Flask:

    http://flask.pocoo.org/
"""

import functools

# pip install Flask
from flask import abort, g, request, redirect, url_for


def login_required(func):
    """Make sure user is logged in before proceeding"""

    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return wrapper_login_required


def validate_json(*expected_args):
    """Validate that a json-request contains the expected parameters"""

    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)

        return wrapper_validate_json

    return decorator_validate_json
