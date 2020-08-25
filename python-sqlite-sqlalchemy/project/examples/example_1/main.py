"""
This is the example 1 program file

This example program was kindly created by Geir Arne Hjelle,
another RealPython author, as part of the editorial process
to improve this article and the information it presents.
You can learn more about Geir from this URL:
https://realpython.com/team/gahjelle/
"""

from importlib import resources

import pandas as pd
from treelib import Tree


def get_data(filepath):
    """Get book data from the csv file"""
    return pd.read_csv(filepath)


def get_books_by_publisher(data, ascending=True):
    """Returns the books by each publisher as a pandas series

    Args:
        data: The pandas dataframe to get the from
        ascending: The sorting direction for the returned data.
        Defaults to True.

    Returns:
        The sorted data as a pandas series
    """
    return data.groupby("publisher").size().sort_values(ascending=ascending)


def get_authors_by_publisher(data, ascending=True):
    """Returns the authors by each publisher as a pandas series

    Args:
        data: The pandas dataframe to get the data from
        ascending: The sorting direction for the returned data.
        Defaults to True.

    Returns:
        The sorted data as a pandas series
    """
    return (
        data.assign(name=data.first_name.str.cat(data.last_name, sep=" "))
        .groupby("publisher")
        .nunique()
        .loc[:, "name"]
        .sort_values(ascending=ascending)
    )


def add_new_book(data, author_name, book_title, publisher_name):
    """Adds a new book to the system"""

    # Does the book exist?
    first_name, _, last_name = author_name.partition(" ")
    if any(
        (data.first_name == first_name)
        & (data.last_name == last_name)
        & (data.title == book_title)
        & (data.publisher == publisher_name)
    ):
        return data
    # Add the new book
    return data.append(
        {
            "first_name": first_name,
            "last_name": last_name,
            "title": book_title,
            "publisher": publisher_name,
        },
        ignore_index=True,
    )


def output_author_hierarchy(data):
    """Output the data as a hierarchy list of authors"""
    authors = data.assign(
        name=data.first_name.str.cat(data.last_name, sep=" ")
    )
    authors_tree = Tree()
    authors_tree.create_node("Authors", "authors")
    for author, books in authors.groupby("name"):
        authors_tree.create_node(author, author, parent="authors")
        for book, publishers in books.groupby("title")["publisher"]:
            book_id = f"{author}:{book}"
            authors_tree.create_node(book, book_id, parent=author)
            for publisher in publishers:
                authors_tree.create_node(publisher, parent=book_id)

    # Output the hierarchical authors data
    authors_tree.show()


def main():
    """The main entry point of the program"""

    # Get the resources for the program
    with resources.path(
        "project.data", "author_book_publisher.csv"
    ) as filepath:
        data = get_data(filepath)

    # Get the number of books printed by each publisher
    books_by_publisher = get_books_by_publisher(data, ascending=False)
    for publisher, total_books in books_by_publisher.items():
        print(f"Publisher: {publisher}, total books: {total_books}")
    print()

    # Get the number of authors each publisher publishes
    authors_by_publisher = get_authors_by_publisher(data, ascending=False)
    for publisher, total_authors in authors_by_publisher.items():
        print(f"Publisher: {publisher}, total authors: {total_authors}")
    print()

    # Output hierarchical authors data
    output_author_hierarchy(data)

    # Add a new book to the data structure
    data = add_new_book(
        data,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )
    # Output the updated hierarchical authors data
    output_author_hierarchy(data)


if __name__ == "__main__":
    main()
