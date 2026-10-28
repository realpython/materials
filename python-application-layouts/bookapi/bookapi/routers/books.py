from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_db

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/")
async def read_books(db: Annotated[dict, Depends(get_db)]):
    return list(db["books"].values())


@router.get("/{book_id}")
async def read_book(book_id: int, db: Annotated[dict, Depends(get_db)]):
    if book_id not in db["books"]:
        raise HTTPException(status_code=404, detail="Book not found")
    return db["books"][book_id]
