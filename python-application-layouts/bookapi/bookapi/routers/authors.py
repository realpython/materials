from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_db

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("/")
async def read_authors(db: Annotated[dict, Depends(get_db)]):
    return list(db["authors"].values())


@router.get("/{author_id}")
async def read_author(author_id: int, db: Annotated[dict, Depends(get_db)]):
    if author_id not in db["authors"]:
        raise HTTPException(status_code=404, detail="Author not found")
    return db["authors"][author_id]
