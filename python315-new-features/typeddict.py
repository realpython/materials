from typing import TypedDict

class Movie(TypedDict, closed=True):
    title: str
    year: int

class Headers(TypedDict, extra_items=str):
    content_type: str

movie: Movie = {"title": "Brazil", "year": 1985, "rating": 8.0}
headers: Headers = {"content_type": "text/html", "x-trace-id": "abc123"}
bad_headers: Headers = {"content_type": "text/html", "x-retries": 3}

print(Movie.__closed__, Headers.__extra_items__)
