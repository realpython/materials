"""
Example 5 program file
"""

from pkg_resources import resource_filename
import sqlite3
from uuid import uuid4
from typing import List
from treelib import Tree


def get_total_number_of_books_by_publishers(connection, direction) -> List:
    """
    :param connection:          connection to the database
    :return:                    List of sorted data
    """
    if direction not in ["asc", "desc"]:
        raise Exception("Unknown direction", direction)

    cursor = connection.cursor()
    sql = f"""
    SELECT
      p.name            as publisher_name,
      count(b.title)    as total_books
    FROM publisher p
    JOIN book_publisher bp on bp.publisher_id = p.publisher_id
    JOIN book b on b.book_id = bp.book_id
    GROUP BY publisher_name
    ORDER BY total_books {direction};
    """
    result = cursor.execute(sql).fetchall()
    return result


def get_total_number_of_authors_by_publishers(connection, direction) -> List:
    """
    :param connection:          connection to the database
    :return:                    List of sorted data
    """
    if direction not in ["asc", "desc"]:
        raise Exception("Unknown direction", direction)

    cursor = connection.cursor()
    sql = f"""
    SELECT
      p.name            as publisher_name,
      count(a.lname)    as total_authors
    FROM publisher p
    JOIN author_publisher ap on p.publisher_id = ap.publisher_id
    JOIN author a on ap.author_id = a.author_id
    GROUP BY publisher_name
    ORDER BY total_authors {direction};
    """
    result = cursor.execute(sql).fetchall()
    return result


def get_authors(connection) -> List:
    """
    This method gets the authors data an builds a hierarchical data
    structure from there for use by the treelib

    :param connection:          connection to the database
    :return:                    list of authors data
    """
    cursor = connection.cursor()
    sql = """
    SELECT
      a.fname || ' ' || a.lname     as author,
      b.title,
      p.name
    FROM author a
    JOIN book b on b.author_id = a.author_id
    JOIN author_publisher ap on ap.author_id = a.author_id
    JOIN publisher p on p.publisher_id = ap.publisher_id
    """
    result = cursor.execute(sql).fetchall()
    # Get the authors
    authors = {row[0]: {} for row in result}
    # Get the books associated with the authors
    for row in result:
        author = row[0]
        title = row[1]
        authors[author][title] = set()
    # Get the publisher associated with the book
    for row in result:
        author = row[0]
        title = row[1]
        publisher = row[2]
        authors[author][title].add(publisher)
    return authors


def add_new_book(connection, author_name, book_title, publisher_name):
    """
    This function adds a new book to the database

    :param session:             database session to work with
    :param author_name:         authors full name
    :param book_title:          book title
    :param publisher_name:      publisher of book
    :return:                    None
    """
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Does the book exist?
    sql = """SELECT 1 FROM book WHERE title = ?"""
    book = cursor.execute(sql, (book_title,)).fetchone()

    if book is not None:
        raise Exception("Book exists", book_title)

    # Get author
    sql = """
        SELECT
          author_id
        FROM author
        WHERE author.fname = ?
        AND author.lname = ?
    """
    fname, lname = author_name.split(" ")
    author = cursor.execute(sql, (fname, lname)).fetchone()

    # Did we get an author?
    if author is None:
        raise Exception("No author found", author_name)

    # Get publisher
    sql = """
        SELECT
          publisher_id
        FROM publisher
        WHERE name = ?
    """
    publisher = cursor.execute(sql, (publisher_name,)).fetchone()

    # Did we get a publisher?
    if publisher is None:
        raise Exception("No publisher found", publisher_name)

    # Add the book
    sql = """
        INSERT INTO book
        (title, author_id)
        VALUES(?, ?)
    """
    book_id = cursor.execute(sql, (book_title, author["author_id"])).lastrowid

    # Update the relationships
    sql = """
        INSERT INTO book_publisher
        (book_id, publisher_id)
        VALUES(?, ?)
    """
    cursor.execute(sql, (book_id, publisher["publisher_id"]))
    connection.commit()


def output_hierarchical_author_data(authors):
    """
    This function outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author, books in authors.items():
        authors_tree.create_node(author, author, parent="authors")
        for book, publishers in books.items():
            authors_tree.create_node(book, book, parent=author)
            for publisher in publishers:
                authors_tree.create_node(publisher, uuid4(), parent=book)
    # Output the hierarchical authors data
    print(authors_tree.show())


def main():
    """
    Main program entry point
    """
    print("starting")

    # connect to the sqlite database
    sqlite_filepath = resource_filename(
        "project.data", "author_book_publisher.db"
    )
    connection = sqlite3.connect(sqlite_filepath)

    # Get the total number of books printed by each publisher
    total_books_by_publisher = get_total_number_of_books_by_publishers(
        connection, "desc"
    )
    for publisher, total_books in total_books_by_publisher:
        print(f"Publisher: {publisher}, total books: {total_books}")
    print()

    # Get the total number of authors each publisher publishes
    total_authors_by_publisher = get_total_number_of_authors_by_publishers(
        connection, "desc"
    )
    for publisher, total_authors in total_authors_by_publisher:
        print(f"Publisher: {publisher}, total authors: {total_authors}")
    print()

    # Output hierarchical authors data
    authors = get_authors(connection)
    output_hierarchical_author_data(authors)

    # add a new book
    add_new_book(
        connection,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )

    # Output hierarchical authors data
    authors = get_authors(connection)
    output_hierarchical_author_data(authors)

    print("finished")


if __name__ == "__main__":
    main()
