"""HTTP API for the bookstore."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from bookstore.catalog import Catalog
from bookstore.inventory import Inventory
from bookstore.pricing import quote_order

app = FastAPI(title="Bookstore")

catalog = Catalog()
inventory = Inventory({isbn: 12 for isbn in catalog.books})


class QuoteRequest(BaseModel):
    isbn: str
    quantity: int = Field(ge=1)
    member_tier: str = "none"
    country: str = "US"


class ReservationRequest(BaseModel):
    isbn: str
    quantity: int = Field(ge=1)


@app.get("/books")
def list_books() -> list[dict]:
    """Return every book in the catalog."""
    return list(catalog.books.values())


@app.get("/books/{isbn}")
def get_book(isbn: str) -> dict:
    """Return a single book by its ISBN."""
    try:
        return catalog.get(isbn)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=exc.args[0]) from None


@app.post("/quotes")
def create_quote(request: QuoteRequest) -> dict:
    """Price an order for one title."""
    try:
        unit_price = catalog.price_of(request.isbn)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=exc.args[0]) from None

    try:
        total = quote_order(
            request.quantity, unit_price, request.member_tier, request.country
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from None

    return {
        "isbn": request.isbn,
        "quantity": request.quantity,
        "total": str(total),
    }


@app.post("/reservations", status_code=201)
def create_reservation(request: ReservationRequest) -> dict:
    """Hold copies of a title for an order."""
    try:
        available = inventory.reserve(request.isbn, request.quantity)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=exc.args[0]) from None
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from None

    return {
        "isbn": request.isbn,
        "reserved": request.quantity,
        "available": available,
    }


@app.get("/stock/{isbn}")
def get_stock(isbn: str) -> dict:
    """Report how many copies are still available."""
    try:
        catalog.get(isbn)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=exc.args[0]) from None
    return {"isbn": isbn, "available": inventory.available(isbn)}
