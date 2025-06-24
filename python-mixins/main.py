import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="\N{rocket} %(message)s"
)

from orm import ActiveRecord, TimestampMixin, SQLMixin


class User(ActiveRecord):
    first_name: str
    last_name: str
    team: bool = False


class Tutorial(SQLMixin, ActiveRecord):
    author: User
    title: str
    url: str


class Comment(TimestampMixin, SQLMixin, ActiveRecord):
    text: str
    tutorial: Tutorial
    user: User | None = None



def populate():
    user = User("Joanna", "Jablonski", team=True)
    user.save()

    tutorial = Tutorial(
        author=user,
        url="https://realpython.com/python-f-strings/",
        title="Python's F-String for String Interpolation and Formatting",
    )
    tutorial.save()

    comment = Comment(
        text="A neutral comment from an anonymous reader",
        tutorial=tutorial,
    )
    comment.save()


if __name__ == "__main__":
    populate()
