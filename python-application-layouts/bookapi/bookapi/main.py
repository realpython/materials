from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin
from .routers import authors, books

app = FastAPI(title="Book Catalog API")

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the book catalog!"}
