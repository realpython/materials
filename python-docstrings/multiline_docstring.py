def get_harry_potter_book(publication_year, title):
    """
    Retrieve a Harry Potter book by its publication year and name.

    Parameters:
    publication_year (int): The year the book was published.
    title (str): The title of the book.

    Returns:
    str: A sentence describing the book and its publication year.
    """
    return f"The book {title!r} was published in the year {publication_year}."
