import json
import re

import pytest

from bookstore.catalog import Catalog

PYTHON_TRICKS = {
    "isbn": "978-1775093305",
    "title": "Python Tricks",
    "author": "Dan Bader",
    "price": "29.99",
}
MANAGING_DEPENDENCIES = {
    "isbn": "978-1775093312",
    "title": "Managing Python Dependencies",
    "author": "Dan Bader",
    "price": "24.99",
}
PYTHON_BASICS = {
    "isbn": "978-1775093329",
    "title": "Python Basics",
    "author": "Real Python",
    "price": "39.99",
}


def write_catalog(path, records):
    path.write_text(json.dumps(records), encoding="utf-8")
    return path


@pytest.fixture
def catalog_path(tmp_path):
    return write_catalog(
        tmp_path / "books.json", [PYTHON_TRICKS, PYTHON_BASICS]
    )


@pytest.fixture
def catalog(catalog_path):
    return Catalog(catalog_path)


def test_catalog_default_path_reads_bundled_books():
    catalog = Catalog()

    result = list(catalog.books)

    assert result == [
        "978-1775093329",
        "978-1775093305",
        "978-1775093312",
        "978-1775093350",
    ]


def test_catalog_missing_file_constructs_without_reading(tmp_path):
    catalog = Catalog(tmp_path / "missing.json")

    assert catalog.path == tmp_path / "missing.json"


def test_catalog_books_missing_file_raises_file_not_found(tmp_path):
    path = tmp_path / "missing.json"
    catalog = Catalog(path)
    message = f"[Errno 2] No such file or directory: '{path}'"

    with pytest.raises(FileNotFoundError, match=f"^{re.escape(message)}$"):
        catalog.books


def test_catalog_books_two_records_returns_dict_by_isbn(catalog):
    result = catalog.books

    assert result == {
        "978-1775093305": PYTHON_TRICKS,
        "978-1775093329": PYTHON_BASICS,
    }


def test_catalog_books_empty_file_returns_empty_dict(tmp_path):
    catalog = Catalog(write_catalog(tmp_path / "books.json", []))

    result = catalog.books

    assert result == {}


def test_catalog_books_file_rewritten_after_read_returns_original(
    catalog, catalog_path
):
    catalog.books
    write_catalog(catalog_path, [MANAGING_DEPENDENCIES])

    result = catalog.books

    assert result == {
        "978-1775093305": PYTHON_TRICKS,
        "978-1775093329": PYTHON_BASICS,
    }


def test_catalog_load_file_rewritten_after_read_returns_new_records(
    catalog, catalog_path
):
    catalog.books
    write_catalog(catalog_path, [MANAGING_DEPENDENCIES])

    catalog.load()

    assert catalog.books == {"978-1775093312": MANAGING_DEPENDENCIES}


def test_catalog_load_valid_file_returns_same_instance(catalog):
    result = catalog.load()

    assert result is catalog


def test_catalog_get_stocked_isbn_returns_record(catalog):
    result = catalog.get("978-1775093329")

    assert result == PYTHON_BASICS


def test_catalog_get_unknown_isbn_raises_key_error(catalog):
    with pytest.raises(KeyError, match="^'unknown isbn: 000'$"):
        catalog.get("000")


def test_catalog_price_of_stocked_isbn_returns_price(catalog):
    result = catalog.price_of("978-1775093329")

    assert result == "39.99"


def test_catalog_price_of_unknown_isbn_raises_key_error(catalog):
    with pytest.raises(KeyError, match="^'unknown isbn: 000'$"):
        catalog.price_of("000")


def test_catalog_by_author_two_books_returns_both_in_order(tmp_path):
    path = write_catalog(
        tmp_path / "books.json",
        [PYTHON_TRICKS, PYTHON_BASICS, MANAGING_DEPENDENCIES],
    )
    catalog = Catalog(path)

    result = catalog.by_author("Dan Bader")

    assert result == [PYTHON_TRICKS, MANAGING_DEPENDENCIES]


def test_catalog_by_author_no_books_returns_empty_list(catalog):
    result = catalog.by_author("Nobody")

    assert result == []
