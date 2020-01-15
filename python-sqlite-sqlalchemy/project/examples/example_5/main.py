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
    Get a list of publishers and the total number of books
    they've published

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
    return cursor.execute(sql).fetchall()


def get_total_number_of_authors_by_publishers(connection, direction) -> List:
    """
    Get a list of publishers and the total number of authors
    they've published
    
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
    return cursor.execute(sql).fetchall()


def get_authors(connection) -> List:
    """
    This method gets the authors data an builds a hierarchical data
    structure from there for use by the treelib

    :param connection:          connection to the database
    :return:                    list of authors data
    """
    cursor = connection.cursor()
    sql = f"""
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


def add_new_item(connection, author_name, book_title, publisher_name):
    """
    This function adds a new item to the database

    :param connection:          connection to the database
    :param author_name:         authors full name
    :param book_title:          book title
    :param publisher_name:      publisher of book
    :return:                    None
    """
    cursor = connection.cursor()

    # Does the author exist in the database?
    sql = """
        SELECT 
            author_id
        FROM author
        WHERE fname = ? AND lname = ?
    """
    fname, lname = author_name.split(" ")
    row = cursor.execute(sql, (fname, lname)).fetchone()
    author_id = row[0] if row is not None else None

    # Does the book exist in the database?
    sql = """
        SELECT 
            book_id
        FROM book
        WHERE title = ?
    """
    row = cursor.execute(sql, (book_title,)).fetchone()
    book_id = row[0] if row is not None else None

    # Does the publisher exist in the database?
    sql = """
        SELECT 
            publisher_id
        FROM publisher
        WHERE name = ?
    """
    row = cursor.execute(sql, (publisher_name,)).fetchone()
    publisher_id = row[0] if row is not None else None

    # Does new item exist?
    if author_id is not None and book_id is not None and publisher_id is not None:
        raise Exception(
            "New item exists", 
            author_name,
            book_title,
            publisher_name
        )
    # Create the author if didn't exist
    if author_id is None:
        sql = """INSERT INTO author (fname, lname) VALUES(?, ?)"""
        cursor.execute(sql, (fname, lname))
        author_id = cursor.lastrowid

    # Create the book if didn't exist
    if book_id is None:
        sql = """
            INSERT INTO book
            (author_id, title)
            VALUES(?, ?)
        """
        cursor.execute(sql, (author_id, book_title))
        book_id = cursor.lastrowid

    # Create the publisher if didn't exist
    if publisher_id is None:
        sql = """INSERT INTO publisher (publisher_name) VALUES(?)"""
        cursor.execute(sql, (publisher_name,))
        publisher_id = cursor.lastrowid

    # Does author publisher association exist?
    sql = """
        SELECT
            1 
        FROM author_publisher 
        WHERE author_id = ?
        AND publisher_id = ?
    """
    row = cursor.execute(sql, (author_id, publisher_id)).fetchone()
    author_publisher_exists = row[0] if row is not None else None

    # Create author publisher association is necessary
    if author_publisher_exists is None:
        sql = """
            INSERT INTO author_publisher
            (author_id, publisher_id)
            VALUES(?, ?)
        """
        cursor.execute(sql, (author_id, publisher_id))

    # Does book publisher association exist?
    sql = """
        SELECT
            1 
        FROM book_publisher
        WHERE book_id = ?
        AND publisher_id = ?
    """
    row = cursor.execute(sql, (book_id, publisher_id)).fetchone()
    book_publisher_exists = row[0] if row is not None else None

    # Create book publisher association is necessary
    if book_publisher_exists is None:
        sql = """
            INSERT INTO book_publisher
            (book_id, publisher_id)
            VALUES(?, ?)
        """
        cursor.execute(sql, (book_id, publisher_id))

    # Commit the transactions to the database
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
    authors_tree.show()


def main():
    """
    Main program entry point
    """
    print("starting")

    # Connect to the sqlite database
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

    # Add a new book
    add_new_item(
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
