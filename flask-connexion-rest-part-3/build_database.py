import os
from config import db
from models import Person, Note

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Doug",
        "lname": "Farrell",
        "notes": [
            "Cool, a mini-blogging application!",
            "This could be useful",
            "Well, sort of useful"
        ]
    },
    {
        "fname": "Kent",
        "lname": "Brockman",
        "notes": [
            "I'm going to make really profound observations",
            "Maybe they'll be more obvious than I thought"
        ]
    },
    {
        "fname": "Bunny",
        "lname": "Easter",
        "notes": [
            "Has anyone seen my Easter eggs?",
            "I'm really late delivering these!"
        ]
    },
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # Add the notes for the person
    for note in person.get("notes"):
        p.notes.append(Note(content=note))
    db.session.add(p)

db.session.commit()
