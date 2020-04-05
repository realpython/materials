"""
This is the example 4 program file
"""

from importlib import resources
from typing import List
from uuid import uuid4

import pandas as pd
from treelib import Tree


def get_author_book_publisher_data(filepath: str) -> pd.DataFrame:
    """Get book data from the csv file"""
    return pd.read_csv(filepath)


def get_total_number_of_books_by_publishers(data, ascending=True) -> List:
    """
    :param data:                author/book/publisher data
    :param direction:           direction to sort the data by
    :return:                    List of sorted data
    """
    return (
        data.loc[:, ["title", "publisher"]]
        .groupby("publisher")["title"]
        .count()
        .sort_values(ascending=ascending)
    )


def get_total_number_of_authors_by_publishers(data, ascending=True) -> List:
    """
    :param data:                author/book/publisher data
    :param direction:           direction to sort the data by
    :return:                    List of sorted data
    """
    return (
        data.assign(name=data.fname.str.cat(data.lname, sep=" "))
        .loc[:, ["name", "publisher"]]
        .groupby("publisher")["name"]
        .nunique()
        .sort_values(ascending=ascending)
    )


def add_new_book(data, author_name, book_title, publisher_name):
    """
    This function adds a new book to the data

    :param data:                author/book/publisher data
    :param author_name:         author's name
    :param book_title:          book title
    :param publisher_name:      publishers name
    :return:                    updated data
    """
    # Does the book exist?
    if book_title in data["title"].values:
        raise Exception("Book exists", book_title)

    # Does the author exist?
    fname, _, lname = author_name.partition(" ")
    if not any(
        data["fname"].str.contains(fname) & data["lname"].str.contains(lname)
    ):
        raise Exception("No author found", author_name)

    # Does the publisher exist?
    if publisher_name not in data["publisher"].values:
        raise Exception("No publisher found", publisher_name)

    # Add the new book
    return data.append(
        {
            "fname": fname,
            "lname": lname,
            "title": book_title,
            "publisher": publisher_name,
        },
        ignore_index=True,
    )


def output_hierarchical_author_data(data):
    """
    This function outputs the author/book/publisher information in
    a hierarchical manner

    :param authors:         the collection of root author objects
    :return:                None
    """
    authors = data.assign(name=data.fname.str.cat(data.lname, sep=" "))

    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author, books in authors.groupby("name"):
        authors_tree.create_node(author, author, parent="authors")
        for book, publishers in books.groupby("title")["publisher"]:
            authors_tree.create_node(book, book, parent=author)
            for publisher in publishers:
                authors_tree.create_node(publisher, uuid4(), parent=book)

    # Output the hierarchical authors data
    authors_tree.show()


def main():
    """
    The main entry point of the program
    """
    print("starting")

    # Connect to the database using SqlAlchemy
    with resources.path(
        "project.data", "author_book_publisher.csv"
    ) as filepath:
        author_book_publisher_data = get_author_book_publisher_data(filepath)

    # Get the total number of books printed by each publisher
    total_books_by_publisher = get_total_number_of_books_by_publishers(
        author_book_publisher_data, ascending=False
    )

    for publisher, total_books in total_books_by_publisher.items():
        print(f"Publisher: {publisher}, total books: {total_books}")
    print()

    # Get the total number of authors each publisher publishes
    total_authors_by_publisher = get_total_number_of_authors_by_publishers(
        author_book_publisher_data, ascending=False
    )
    for publisher, total_authors in total_authors_by_publisher.items():
        print(f"Publisher: {publisher}, total authors: {total_authors}")
    print()

    # Output hierarchical authors data
    output_hierarchical_author_data(author_book_publisher_data)

    # Add a new book to the data structure
    author_book_publisher_data = add_new_book(
        author_book_publisher_data,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )

    # Output the updated hierarchical authors data
    output_hierarchical_author_data(author_book_publisher_data)

    print("finished")


if __name__ == "__main__":
    main()
