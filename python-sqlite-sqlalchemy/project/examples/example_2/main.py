"""
This program gathers information from the author_book_publisher.db
SQLite database file
"""

from importlib import resources

from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func

from project.modules.models import Author, Book, Publisher
from treelib import Tree


def get_books_by_publishers(session, ascending=True):
    """Get a list of publishers and the number of books they've published

    Args:
        session: database session to use
        ascending: direction to sort the results

    Returns:
        List: list of publisher sorted by number of books published
    """
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")

    direction = asc if ascending else desc

    return (
        session.query(
            Publisher.name, func.count(Book.title).label("total_books")
        )
        .join(Publisher.books)
        .group_by(Publisher.name)
        .order_by(direction("total_books"))
    )


def get_authors_by_publishers(session, ascending=True):
    """Get a list of publishers and the number of authors they've published

    Args:
        session: database session to use
        ascending: direction to sort the results

    Returns:
        List: list of publisher sorted by number of authors published
    """
    if not isinstance(ascending, bool):
        raise ValueError(f"Sorting value invalid: {ascending}")

    direction = asc if ascending else desc

    return (
        session.query(
            Publisher.name,
            func.count(Author.first_name).label("total_authors"),
        )
        .join(Publisher.authors)
        .group_by(Publisher.name)
        .order_by(direction("total_authors"))
    )


def get_authors(session):
    """Get a list of author objects sorted by last name"""
    return session.query(Author).order_by(Author.last_name).all()


def add_new_book(session, author_name, book_title, publisher_name):
    """Adds a new book to the system"""

    # Get the author's first and last names
    first_name, _, last_name = author_name.partition(" ")

    # Check if the book exists
    book = (
        session.query(Book)
        .join(Author)
        .filter(Book.title == book_title)
        .filter(
            and_(
                Author.first_name == first_name, Author.last_name == last_name
            )
        )
        .filter(Book.publishers.any(Publisher.name == publisher_name))
        .one_or_none()
    )
    # Does the book by the author and publisher already exist?
    if book is not None:
        return

    # Check if the book exists for the author
    book = (
        session.query(Book)
        .join(Author)
        .filter(Book.title == book_title)
        .filter(
            and_(
                Author.first_name == first_name, Author.last_name == last_name
            )
        )
        .one_or_none()
    )
    # Create the new book if needed
    if book is None:
        book = Book(title=book_title)

    # Get the author
    author = (
        session.query(Author)
        .filter(
            and_(
                Author.first_name == first_name, Author.last_name == last_name
            )
        )
        .one_or_none()
    )
    # Do we need to create the author?
    if author is None:
        author = Author(first_name=first_name, last_name=last_name)
        session.add(author)

    # Get the publisher
    publisher = (
        session.query(Publisher)
        .filter(Publisher.name == publisher_name)
        .one_or_none()
    )
    # Do we need to create the publisher?
    if publisher is None:
        publisher = Publisher(name=publisher_name)
        session.add(publisher)

    # Initialize the book relationships
    book.author = author
    book.publishers.append(publisher)
    session.add(book)

    # Commit to the database
    session.commit()


def output_author_hierarchy(authors):
    """
    Outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author in authors:
        author_id = f"{author.first_name} {author.last_name}"
        authors_tree.create_node(author_id, author_id, parent="authors")
        for book in author.books:
            book_id = f"{author_id}:{book.title}"
            authors_tree.create_node(book.title, book_id, parent=author_id)
            for publisher in book.publishers:
                authors_tree.create_node(publisher.name, parent=book_id)
    # Output the hierarchical authors data
    authors_tree.show()


def main():
    """Main entry point of program"""

    # Connect to the database using SQLAlchemy
    with resources.path(
        "project.data", "author_book_publisher.db"
    ) as sqlite_filepath:
        engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Get the number of books printed by each publisher
    books_by_publisher = get_books_by_publishers(session, ascending=False)
    for row in books_by_publisher:
        print(f"Publisher: {row.name}, total books: {row.total_books}")
    print()

    # Get the number of authors each publisher publishes
    authors_by_publisher = get_authors_by_publishers(session)
    for row in authors_by_publisher:
        print(f"Publisher: {row.name}, total authors: {row.total_authors}")
    print()

    # Output hierarchical authors data
    authors = get_authors(session)
    output_author_hierarchy(authors)

    # Add a new book
    add_new_book(
        session,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )
    # Output the updated hierarchical authors data
    authors = get_authors(session)
    output_author_hierarchy(authors)


if __name__ == "__main__":
    main()
