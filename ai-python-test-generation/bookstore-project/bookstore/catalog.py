"""Book records loaded from a JSON file on disk."""

import json
from pathlib import Path

DEFAULT_CATALOG_PATH = Path(__file__).parent / "data" / "books.json"


class Catalog:
    """Read-only access to the book records in a JSON catalog file."""

    def __init__(self, path=None):
        self.path = Path(path) if path is not None else DEFAULT_CATALOG_PATH
        self._books = None

    def load(self):
        """Read and parse the catalog file."""
        text = self.path.read_text(encoding="utf-8")  # pragma: no mutate
        records = json.loads(text)
        self._books = {record["isbn"]: record for record in records}
        return self

    @property
    def books(self):
        """All records, loading the file on first access."""
        if self._books is None:
            self.load()
        return self._books

    def get(self, isbn):
        """Return one record, or raise if the ISBN is not stocked."""
        try:
            return self.books[isbn]
        except KeyError:
            raise KeyError(f"unknown isbn: {isbn}") from None

    def price_of(self, isbn):
        """Return the list price of one book."""
        return self.get(isbn)["price"]

    def by_author(self, author):
        """Return every record by an author, in catalog order."""
        return [
            book for book in self.books.values() if book["author"] == author
        ]
