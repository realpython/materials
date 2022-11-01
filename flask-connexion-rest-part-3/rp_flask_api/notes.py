from flask import make_response, abort

from config import db
from models import (
    Note,
    NoteSchema,
    Person,
)


def read_one(note_id):
    note = Note.query.get(note_id)

    if note is not None:
        note_schema = NoteSchema()
        return note_schema.dump(note)
    else:
        abort(404, f"Note with ID {note_id} not found")


def update(note_id, note):
    existing_note = Note.query.get(note_id)

    if existing_note:
        schema = NoteSchema()
        update_note = schema.load(note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {note_id} not found")


def delete(note_id):
    existing_note = Note.query.get(note_id)

    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 200)
    else:
        abort(404, f"Note with ID {note_id} not found")


def create(note):
    person_id = note.get("person_id")
    person = Person.query.get(person_id)

    if person:
        schema = NoteSchema()
        new_note = schema.load(note, session=db.session)
        person.notes.append(new_note)
        db.session.commit()
        return schema.dump(new_note), 201
    else:
        abort(404, f"Person not found for ID: {person_id}")
