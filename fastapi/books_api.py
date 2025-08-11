from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = [
    {"id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635},
    {"id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99},
]

class Book(BaseModel):
    title: str
    author: str
    pages: int

@app.get("/books")
def get_books(limit: Optional[int] = None):
    """Get all books, optionally limited by count."""
    if limit:
        return {"books": books[:limit]}
    return {"books": books}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Get a specific book by ID."""
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
def create_book(book: Book):
    """Create a new book entry."""
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }
    books.append(new_book)
    return new_book
