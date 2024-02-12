import functools

from flask import Flask, abort, request

app = Flask(__name__)


def validate_json(*expected_args):
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


@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()  # noqa
    # Update database.
    return "success!"
