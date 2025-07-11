def get_harry_potter_books(publication_year, book_name):
    """
    Retrieve a Harry Potter book by its publication year and name.

    Parameters:
    publication_year (int): The year the book was published.
    book_name (str): The name of the book.

    Returns:
    str: A sentence describing the book and its publication year.
    """
    return (
        f"The book {book_name} was published in the year {publication_year}."
    )
