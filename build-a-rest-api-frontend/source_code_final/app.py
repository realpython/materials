from flask import render_template
import config
from models import Person

import sys

app = config.connex_app
app.add_api("swagger.yml")


@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)


@app.route("/<person_name>")
def person(person_name):
    print(person_name, file=sys.stderr)
    person_object = Person.query.order_by(
        Person.fname.ilike("person_name")
    ).first()
    print(person_object.fname, file=sys.stderr)
    return render_template("person.html", person=person_object)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
