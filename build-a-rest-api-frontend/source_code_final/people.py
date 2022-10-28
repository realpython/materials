from flask import make_response, abort

from config import db
from models import (
    Person,
    PersonSchema,
)


def read_all():
    people = Person.query.all()
    person_schema = PersonSchema(many=True)
    return person_schema.dump(people)


def create(person):
    schema = PersonSchema()
    new_person = schema.load(person, session=db.session)
    db.session.add(new_person)
    db.session.commit()
    return schema.dump(new_person), 201


def read_one(person_id):
    person = Person.query.get(person_id)

    if person is not None:
        person_schema = PersonSchema()
        return person_schema.dump(person)
    else:
        abort(404, f"Person with ID {person_id} not found")


def update(person_id, person):
    existing_person = Person.query.get(person_id)

    if existing_person:
        schema = PersonSchema()
        update_person = schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return schema.dump(existing_person), 201
    else:
        abort(404, f"Person with ID {person_id} not found")


def delete(person_id):
    existing_person = Person.query.get(person_id)

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{person_id} successfully deleted", 200)
    else:
        abort(404, f"Person with ID {person_id} not found")
