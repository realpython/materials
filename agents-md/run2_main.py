import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
cars: list[dict] = json.loads(Path("cars.json").read_text())


class NewCar(BaseModel):
    make: str
    model: str
    year: int
    horsepower: int
    engine_cc: int
    transmission: str


@app.get("/cars")
def list_cars() -> list[dict]:
    """Return a list of all cars."""
    return cars


@app.get("/cars/{car_id}")
def get_car(car_id: int) -> dict:
    """Return a single car by its id, or raise 404 if it doesn't exist."""
    for car in cars:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Car not found")


@app.post("/cars", status_code=201)
def create_car(new_car: NewCar) -> dict:
    """Add a new car and return it with a server-assigned id."""
    car = new_car.model_dump()
    car["id"] = max((existing["id"] for existing in cars), default=0) + 1
    cars.append(car)
    return car


@app.delete("/cars/{car_id}", status_code=204)
def delete_car(car_id: int) -> None:
    """Delete a car by its id, or raise 404 if it doesn't exist."""
    for index, car in enumerate(cars):
        if car["id"] == car_id:
            del cars[index]
            return
    raise HTTPException(status_code=404, detail="Car not found")
