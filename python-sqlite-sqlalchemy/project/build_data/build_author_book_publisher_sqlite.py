"""
This program builds the author_book_publisher Sqlite database from the
author_book_publisher.csv file.
"""

import os
import csv
from importlib import resources
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project.modules.models import Base
from project.modules.models import Author
from project.modules.models import Book
from project.modules.models import Publisher


def get_author_book_publisher_data(filepath):
    """
    This function gets the data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data


def populate_database(session, author_book_publisher_data):
    # insert the data
    for row in author_book_publisher_data:

        author = (
            session.query(Author)
            .filter(Author.last_name == row["last_name"])
            .one_or_none()
        )
        if author is None:
            author = Author(
                first_name=row["first_name"], last_name=row["last_name"]
            )
            session.add(author)

        book = (
            session.query(Book)
            .filter(Book.title == row["title"])
            .one_or_none()
        )
        if book is None:
            book = Book(title=row["title"])
            session.add(book)

        publisher = (
            session.query(Publisher)
            .filter(Publisher.name == row["publisher"])
            .one_or_none()
        )
        if publisher is None:
            publisher = Publisher(name=row["publisher"])
            session.add(publisher)

        # add the items to the relationships
        author.books.append(book)
        author.publishers.append(publisher)
        publisher.authors.append(author)
        publisher.books.append(book)
        session.commit()

    session.close()


def main():
    print("starting")

    # get the author/book/publisher data into a dictionary structure
    with resources.path(
        "project.data", "author_book_publisher.csv"
    ) as csv_filepath:
        data = get_author_book_publisher_data(csv_filepath)
        author_book_publisher_data = data

    # get the filepath to the database file
    with resources.path(
        "project.data", "author_book_publisher.db"
    ) as sqlite_filepath:
        # does the database exist?
        if os.path.exists(sqlite_filepath):
            os.remove(sqlite_filepath)

    # create the database
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    populate_database(session, author_book_publisher_data)

    print("finished")


if __name__ == "__main__":
    main()
