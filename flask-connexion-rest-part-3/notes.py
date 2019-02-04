"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Person, Note, NoteSchema


def read_all():
    """
    This function responds to a request for /api/people/notes
    with the complete list of notes, sorted by note timestamp

    :return:                json list of all notes for all people
    """
    # Query the database for all the notes
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    # Serialize the list of notes from our data
    note_schema = NoteSchema(many=True, exclude=["person.notes"])
    data = note_schema.dump(notes).data
    return data


def read_one(person_id, note_id):
    """
    This function responds to a request for
    /api/people/{person_id}/notes/{note_id}
    with one matching note for the associated person

    :param person_id:       Id of person the note is related to
    :param note_id:         Id of the note
    :return:                json string of note contents
    """
    # Query the database for the note
    note = (
        Note.query.join(Person, Person.person_id == Note.person_id)
        .filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # Was a note found?
    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note).data
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {note_id}")


def create(person_id, note):
    """
    This function creates a new note related to the passed in person id.

    :param person_id:       Id of the person the note is related to
    :param note:            The JSON containing the note data
    :return:                201 on success
    """
    # get the parent person
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # Was a person found?
    if person is None:
        abort(404, f"Person not found for Id: {person_id}")

    # Create a note schema instance
    schema = NoteSchema()
    new_note = schema.load(note, session=db.session).data

    # Add the note to the person and database
    person.notes.append(new_note)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_note).data

    return data, 201


def update(person_id, note_id, note):
    """
    This function updates an existing note related to the passed in
    person id.

    :param person_id:       Id of the person the note is related to
    :param note_id:         Id of the note to update
    :param content:            The JSON containing the note data
    :return:                200 on success
    """
    update_note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # Did we find an existing note?
    if update_note is not None:

        # turn the passed in note into a db object
        schema = NoteSchema()
        update = schema.load(note, session=db.session).data

        # Set the id's to the note we want to update
        update.person_id = update_note.person_id
        update.note_id = update_note.note_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated note in the response
        data = schema.dump(update_note).data

        return data, 200

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {note_id}")


def delete(person_id, note_id):
    """
    This function deletes a note from the note structure

    :param person_id:   Id of the person the note is related to
    :param note_id:     Id of the note to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the note requested
    note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # did we find a note?
    if note is not None:
        db.session.delete(note)
        db.session.commit()
        return make_response(
            "Note {note_id} deleted".format(note_id=note_id), 200
        )

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Note not found for Id: {note_id}")
