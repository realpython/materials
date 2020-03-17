
from flask import render_template
from flask import request
from flask import redirect
from app import app


@app.route("/")
def hello_world():
    return "Hello World"


