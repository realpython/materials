"""
This program gathers information from the temp_data.csv file about temperature
"""

from pkg_resources import resource_filename
from typing import List
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy.sql import func, asc, desc
from sqlalchemy.orm import sessionmaker
from treelib import Tree
from project.modules.models import Author
from project.modules.models import Book
from project.modules.models import Publisher


def get_total_number_of_books_by_publishers(session, direction: str) -> List:
    """

    :param session:             database session to work with
    :param direction:
    :return:
    """
    if direction not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    dir = desc if direction == "desc" else asc

    results = (
        session.query(
            Publisher.name, func.count(Book.title).label("total_books")
        )
        .join(Publisher.books)
        .group_by(Publisher.name)
        .order_by(dir("total_books"))
    )
    return results


def get_total_number_of_authors_by_publishers(session, direction: str) -> List:
    """

    :param session:             database session to work with
    :param direction:
    :return:
    """
    if direction not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    dir = desc if direction == "desc" else asc

    results = (
        session.query(
            Publisher.name, func.count(Author.fname).label("total_authors")
        )
        .join(Publisher.authors)
        .group_by(Publisher.name)
        .order_by(dir("total_authors"))
    )
    return results


def get_authors(session) -> List:
    """
    This function returns a list of author objects

    :param session:             database session to work with
    :return:                    list of Author objects
    """
    results = session.query(Author).order_by(Author.lname).all()
    return results


def add_new_book(session, author_name, book_title, publisher_name):
    """
    This function adds a new book to the database

    :param session:             database session to work with
    :param author_name:         authors full name
    :param book_title:          book title
    :param publisher_name:      publisher of book
    :return:                    None
    """
    fname, lname = author_name.split(" ")

    # Does the book exist?
    book = session.query(Book).filter(Book.title == book_title).one_or_none()
    if book is not None:
        raise Exception("Book exists", book_title)

    # Get author
    author = (
        session.query(Author)
        .filter(and_(Author.fname == fname, Author.lname == lname))
        .one_or_none()
    )

    # Did we get an author?
    if author is None:
        raise Exception("No author found", author_name)

    # Get publisher
    publisher = (
        session.query(Publisher)
        .filter(Publisher.name == publisher_name)
        .one_or_none()
    )

    # Did we get a publisher?
    if publisher is None:
        raise Exception("No publisher found", publisher)

    # Create the book
    new_book = Book(title=book_title)

    # Insert the book and create the relationships
    author.books.append(new_book)
    publisher.books.append(new_book)
    session.commit()


def output_hierarchical_author_data(authors):
    """
    This function outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author in authors:
        authors_tree.create_node(
            f"{author.fname} {author.lname}",
            f"{author.fname} {author.lname}",
            parent="authors",
        )
        for book in author.books:
            authors_tree.create_node(
                f"{book.title}",
                f"{book.title}",
                parent=f"{author.fname} {author.lname}",
            )
            for publisher in book.publishers:
                authors_tree.create_node(
                    f"{publisher.name}", uuid4(), parent=f"{book.title}"
                )
    # Output the hierarchical authors data
    print(authors_tree.show())


def main():
    """
    Main entry point of program
    """
    print("starting")

    # Connect to the database using SqlAlchemy
    sqlite_filepath = resource_filename(
        "project.data", "author_book_publisher.db"
    )
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Get the total number of books printed by each publisher
    total_books_by_publisher = get_total_number_of_books_by_publishers(
        session, "desc"
    )
    for row in total_books_by_publisher:
        print(f"Publisher: {row.name}, total books: {row.total_books}")
    print()

    # Get the total number of authors each publisher publishes
    total_authors_by_publisher = get_total_number_of_authors_by_publishers(
        session, "desc"
    )
    for row in total_authors_by_publisher:
        print(f"Publisher: {row.name}, total authors: {row.total_authors}")
    print()

    # Output hierarchical authors data
    authors = get_authors(session)
    output_hierarchical_author_data(authors)

    # Add a new book
    add_new_book(
        session,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )

    # Output the updated hierarchical authors data
    authors = get_authors(session)
    output_hierarchical_author_data(authors)

    print("finished")


if __name__ == "__main__":
    main()
