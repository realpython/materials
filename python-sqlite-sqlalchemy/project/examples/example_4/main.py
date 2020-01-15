"""
This is the example 4 program file
"""

import csv
import copy
from pkg_resources import resource_filename
from typing import List
from collections import defaultdict
from uuid import uuid4
from treelib import Tree


def get_author_book_publisher_data(filepath: str) -> List:
    """
    This function gets the temperature data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
        return data


def get_total_number_of_books_by_publishers(data, direction) -> List:
    """
    :param data:                author/book/publisher data
    :param direction:           direction to sort the data by
    :return:                    List of sorted data
    """
    if direction not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    # Get total number of books for each publisher
    publishers = defaultdict(int)
    for row in data:
        publishers[row["publisher"]] += 1

    # Convert the dictionary to a list of tuples and sort it
    return sorted(
        [(k, v) for k, v in publishers.items()],
        key=lambda v: v[1],
        reverse=False if direction == "asc" else True,
    )


def get_total_number_of_authors_by_publishers(data, direction: str) -> List:
    """
    :param data:                author/book/publisher data
    :param direction:           direction to sort the data by
    :return:                    List of sorted data
    """
    if direction not in ["asc", "desc"]:
        raise Exception("Unknown direction", direction)

    # Get total number of authors for each publisher
    publishers = defaultdict(list)
    for row in data:
        publishers[row["publisher"]] = []

    for row in data:
        author = f"{row['fname']} {row['lname']}"
        if author not in publishers[row["publisher"]]:
            publishers[row["publisher"]].append(author)

    return sorted(
        [(k, len(v)) for k, v in publishers.items()],
        key=lambda v: v[1],
        reverse=False if direction == "asc" else True,
    )


def get_authors(data) -> List:
    """
    This function returns a list of authors, including their hierarchical
    data

    :param data:                author/book/publisher data
    :return:                    list of authors data
    """
    # Get the authors
    authors = {f"{row['fname']} {row['lname']}": {} for row in data}
    # Get the books associated with the authors
    for row in data:
        author = f"{row['fname']} {row['lname']}"
        title = row["title"]
        authors[author][title] = set()
        publisher = row["publisher"]
        authors[author][title].add(publisher)
    return authors


def add_new_item(data, author_name, book_title, publisher_name):
    """
    This function adds a new item (author, book, publisher) to the data

    :param data:                author/book/publisher data
    :param author_name:         author's name
    :param book_title:          book title
    :param publisher_name:      publishers name
    :return:                    updated data
    """
    # Iterate through the data
    new_item_exists = False
    for row in data:
        author_exists = author_name == f"{row['fname']} {row['lname']}"
        book_exists = book_title == row["title"]
        publisher_exists = publisher_name == row["publisher"]

        # Set new_item_exists flag if new item found in data
        if author_exists and book_exists and publisher_exists:
            new_item_exists = True
            break
        
    # Does the new item exist already?
    if new_item_exists:            
        raise Exception("New item exists", author_name, book_title, publisher_name)

    # Don't modify the input data
    new_data = copy.deepcopy(data)

    # Add the new item
    fname, lname = author_name.split(" ")
    new_data.append({
        "fname": fname,
        "lname": lname,
        "title": book_title,
        "publisher": publisher_name
    })
    return new_data

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
    The main entry point of the program
    """
    print("starting")

    # get the data into memory
    filepath = resource_filename("project.data", "author_book_publisher.csv")
    author_book_publisher_data = get_author_book_publisher_data(filepath)

    # Get the total number of books printed by each publisher
    total_books_by_publisher = get_total_number_of_books_by_publishers(
        author_book_publisher_data, "desc"
    )
    for publisher, total_books in total_books_by_publisher:
        print(f"Publisher: {publisher}, total books: {total_books}")
    print()

    # Get the total number of authors each publisher publishes
    total_authors_by_publisher = get_total_number_of_authors_by_publishers(
        author_book_publisher_data, "desc"
    )
    for publisher, total_authors in total_authors_by_publisher:
        print(f"Publisher: {publisher}, total authors: {total_authors}")
    print()

    # Output hierarchical authors data
    authors = get_authors(author_book_publisher_data)
    output_hierarchical_author_data(authors)

    # Add a new book to the data structure
    author_book_publisher_data = add_new_item(
        author_book_publisher_data,
        author_name="Stephen King",
        book_title="The Stand",
        publisher_name="Random House",
    )
    # Output the updated hierarchical authors data
    authors = get_authors(author_book_publisher_data)
    output_hierarchical_author_data(authors)

    print("finished")


if __name__ == "__main__":
    main()
