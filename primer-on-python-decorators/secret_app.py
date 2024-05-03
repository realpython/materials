import functools

from flask import Flask, g, redirect, request, url_for

app = Flask(__name__)


def login_required(func):
    """Make sure user is logged in before proceeding"""

    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return wrapper_login_required


@app.route("/secret")
@login_required
def secret(): ...
