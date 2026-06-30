import json
import os

from fastapi import FastAPI, HTTPException

app = FastAPI()

data_file = os.path.join(os.path.dirname(__file__), "cars.json")
with open(data_file) as f:
    cars = json.load(f)


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


@app.post("/cars")
def create_car(car: dict):
    car["id"] = len(cars) + 1
    cars.append(car)
    return {"message": "Car created successfully", "car": car}


@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for i in range(len(cars)):
        if cars[i]["id"] == car_id:
            cars.pop(i)
            return {"message": "Car deleted"}
    return {"error": "Car not found"}
