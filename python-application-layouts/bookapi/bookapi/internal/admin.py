from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_catalog():
    return {"message": "Catalog updated"}
