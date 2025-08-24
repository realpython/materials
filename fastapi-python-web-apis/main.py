import random
from string import ascii_letters, hexdigits
from typing import Annotated

from jinja2 import Template
from pydantic import BaseModel, Field

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, PlainTextResponse

tags_metadata = [
    {
        "name": "Random Playground",
        "description": "Operations for generating random stuff",
    },
    {
        "name": "Random Items Management",
        "description": "Create, shuffle, read, update and delete items",
    },
]

app = FastAPI(
    title="Randomizer API",
    description="Generate random numbers and manage a list of items",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

items_db = []


class Item(BaseModel):
    name: str = Field(
        min_length=1, max_length=100, description="The item name"
    )


class ItemList(BaseModel):
    items: list[str] = Field(min_items=1, description="List of items")


class ItemUpdate(BaseModel):
    old_item: str = Field(min_length=1, description="Item to replace")
    new_item: str = Field(min_length=1, description="New item name")


class ItemResponse(BaseModel):
    message: str
    item: str
    total_items: int


class ItemListResponse(BaseModel):
    original_order: list[str]
    randomized_order: list[str]
    count: int


class ItemUpdateResponse(BaseModel):
    message: str
    old_item: str
    new_item: str


class ItemDeleteResponse(BaseModel):
    message: str
    deleted_item: str
    remaining_items: int


@app.get("/", tags=["Random Playground"])
async def home():
    return {"message": "Welcome to the Randomizer API"}


@app.get("/random/{max_value}", tags=["Random Playground"])
async def get_random_number(max_value: int):
    return {"max": max_value, "random_number": random.randint(1, max_value)}


@app.get("/random-between", tags=["Random Playground"])
def get_random_number_between(
    min_value: Annotated[
        int | None,
        Query(
            title="Minimum Value",
            description="The minimum random number",
            ge=1,
            le=99,
        ),
    ] = 1,
    max_value: Annotated[
        int | None,
        Query(
            title="Maximum Value",
            description="The maximum random number",
            ge=1,
            le=1000,
        ),
    ] = 99,
):
    if min_value > max_value:
        return {"error": "min_value cannot be greater than max_value"}

    return {
        "min": min_value,
        "max": max_value,
        "random_number": random.randint(min_value, max_value),
    }


@app.get("/random-string/{length}", tags=["Random Playground"])
def generate_random_string(length: int):
    return PlainTextResponse("".join(random.choices(ascii_letters, k=length)))


@app.get(
    "/random-color", response_class=HTMLResponse, tags=["Random Playground"]
)
def random_color():
    hex_chars = "".join(random.choice(hexdigits.lower()) for _ in range(6))
    hex_color = f"#{hex_chars}"
    template_string = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Random Color: {{ color }}</title>
        <style>
            body {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: {{ color }};
                color: white;
                font-size: 120px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div>{{ color }}</div>
    </body>
    </html>
    """

    template = Template(template_string)
    html_content = template.render(color=hex_color)

    return html_content


@app.post(
    "/items", response_model=ItemResponse, tags=["Random Items Management"]
)
def add_item(item: Item):
    if item.name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    items_db.append(item.name)
    return ItemResponse(
        message="Item added successfully",
        item=item.name,
        total_items=len(items_db),
    )


@app.get(
    "/items/random",
    response_model=ItemListResponse,
    tags=["Random Items Management"],
)
def get_randomized_items():
    if not items_db:
        return ItemListResponse(
            original_order=[], randomized_order=[], count=0
        )

    randomized = items_db.copy()
    random.shuffle(randomized)

    return ItemListResponse(
        original_order=items_db,
        randomized_order=randomized,
        count=len(items_db),
    )


@app.put(
    "/items",
    response_model=ItemUpdateResponse,
    tags=["Random Items Management"],
)
def update_item(item_update: ItemUpdate):
    if item_update.old_item not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    index = items_db.index(item_update.old_item)
    items_db[index] = item_update.new_item

    return ItemUpdateResponse(
        message="Item updated successfully",
        old_item=item_update.old_item,
        new_item=item_update.new_item,
    )


@app.delete(
    "/items/{item}",
    response_model=ItemDeleteResponse,
    tags=["Random Items Management"],
)
def delete_item(item: str):
    if item not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    items_db.remove(item)

    return ItemDeleteResponse(
        message="Item deleted successfully",
        deleted_item=item,
        remaining_items=len(items_db),
    )
