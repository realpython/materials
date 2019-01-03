from datetime import datetime
from config import db, ma
from marshmallow import fields



class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship('Note',
                            backref='person',
                            cascade='all, delete-orphan',
                            lazy='noload',
                            order_by='desc(Note.timestamp)')


class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
    notes = fields.Nested('NoteSchema', default=[], many=True)


class NoteSchema(ma.ModelSchema):
    class Meta:
        model = Note
        sqla_session = db.session
