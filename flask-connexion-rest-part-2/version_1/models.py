from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


# flask-marshmallow<0.12.0

# class PersonSchema(ma.ModelSchema):
#    class Meta:
#        model = Person
#        sqla_session = db.session

# flask-marshmallow>=0.12.0 (recommended)
class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session
