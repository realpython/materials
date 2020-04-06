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
    Get a list of publishers and the total number of books
    they've published

    :param session:             database session to work with
    :param direction:
    :return:
    """
    if direction not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    dir = desc if direction == "desc" else asc

    return (
        session.query(
            Publisher.name, func.count(Book.title).label("total_books")
        )
        .join(Publisher.books)
        .group_by(Publisher.name)
        .order_by(dir("total_books"))
    )


def get_total_number_of_authors_by_publishers(session, direction: str) -> List:
    """
    Get a list of publishers and the total number of authors
    they've published

    :param session:             database session to work with
    :param direction:
    :return:
    """
    if direction not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    dir = desc if direction == "desc" else asc

    return (
        session.query(
            Publisher.name, func.count(Author.fname).label("total_authors")
        )
        .join(Publisher.authors)
        .group_by(Publisher.name)
        .order_by(dir("total_authors"))
    )


def get_authors(session) -> List:
    """
    This function returns a list of author objects

    :param session:             database session to work with
    :return:                    list of Author objects
    """
    return session.query(Author).order_by(Author.lname).all()


def add_new_item(session, author_name, book_title, publisher_name):
    """
    This function adds a new item to the database

    :param session:             database session to work with
    :param author_name:         authors full name
    :param book_title:          book title
    :param publisher_name:      publisher of book
    :return:                    None
    """
    # Get the author if exists
    fname, lname = author_name.split(" ")
    author = (
        session.query(Author)
        .filter(and_(Author.fname == fname, Author.lname == lname))
        .one_or_none()
    )

    # Get the book if exists
    book = session.query(Book).filter(Book.title == book_title).one_or_none()

    # Get the publisher if exists
    publisher = (
        session.query(Publisher)
        .filter(Publisher.name == publisher_name)
        .one_or_none()
    )
    # Does new item exist?
    if author is not None and book is not None and publisher is not None:
        raise Exception(
            "New item exists", author_name, book_title, publisher_name
        )
    # Create the author if didn't exist
    if author is None:
        author = Author(fname=fname, lname=lname)

    # Create the book if didn't exist
    if book is None:
        book = Book(title=book_title)

    # Create the publisher if didn't exist
    if publisher is None:
        publisher = Publisher(name=publisher_name)

    # Add the book to the author's books collection if didn't exist
    if book not in author.books:
        author.books.append(book)

    # Add the author to the publisher's collection if didn't exist
    if author not in publisher.authors:
        publisher.authors.append(author)

    # Add the book to the publisher's collection if didn't exist
    if book not in publisher.books:
        publisher.books.append(book)

    # Commit to the database
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
    authors_tree.show()


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
    add_new_item(
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
