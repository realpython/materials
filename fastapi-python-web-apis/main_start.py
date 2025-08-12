from fastapi import FastAPI

app = FastAPI()

items_db = []


@app.get("/")
def home():
    return {"message": "Welcome to the Randomizer API"}


@app.post("/items")
def add_item(item: str):
    if not item.strip():
        raise HTTPException(status_code=400, detail="Item cannot be empty")

    if item in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db.append(item)
    return {
        "message": "Item added successfully",
        "item": item,
        "total_items": len(items_db),
    }
