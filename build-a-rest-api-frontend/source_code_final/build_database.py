from datetime import datetime
from config import app, db
from models import Person, Note

PEOPLE_NOTES = [
    {
        "lname": "Fairy",
        "fname": "Sugar",
        "notes": [
            ("Cool, a mini-blogging application!", "2022-01-06 22:17:54"),
            ("This could be useful", "2022-01-08 22:17:54"),
            ("Well, sort of useful", "2022-03-06 22:17:54"),
        ],
    },
    {
        "lname": "Ruprecht",
        "fname": "Knecht",
        "notes": [
            (
                "I'm going to make really profound observations",
                "2022-01-07 22:17:54",
            ),
            (
                "Maybe they'll be more obvious than I thought",
                "2022-02-06 22:17:54",
            ),
        ],
    },
    {
        "lname": "Bunny",
        "fname": "Easter",
        "notes": [
            ("Has anyone seen my Easter eggs?", "2022-01-07 22:47:54"),
            ("I'm really late delivering these!", "2022-04-06 22:17:54"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in PEOPLE_NOTES:
        new_person = Person(lname=data.get("lname"), fname=data.get("fname"))
        for note in data.get("notes"):
            content, timestamp = note
            new_person.notes.append(
                Note(
                    content=content,
                    timestamp=datetime.strptime(
                        timestamp, "%Y-%m-%d %H:%M:%S"
                    ),
                )
            )
        db.session.add(new_person)

    db.session.commit()
