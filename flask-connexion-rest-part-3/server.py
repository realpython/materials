"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# Local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


# Create a URL route in our application for "/people"
@connex_app.route("/people")
def people():
    """
    This function just responds to the browser URL
    localhost:5000/people

    :return:        the rendered template "people.html"
    """
    return render_template("people.html")


# Create a URL route to the notes page
@connex_app.route("/notes/<int:person_id>")
def notes(person_id):
    """
    This function responds to the browser URL
    localhost:5000/notes/<person_id>

    :param person_id:   Id of the person to show notes for
    :return:            the rendered template "notes.html"
    """
    return render_template("notes.html", person_id=person_id)


if __name__ == "__main__":
    connex_app.run(debug=True)
