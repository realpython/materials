from fastapi.testclient import TestClient

from run2_main import app, cars

client = TestClient(app)


def test_create_car_assigns_unique_id():
    new_car = {
        "make": "Honda",
        "model": "Civic",
        "year": 2021,
        "horsepower": 158,
        "engine_cc": 1996,
        "transmission": "Manual",
    }
    response = client.post("/cars", json=new_car)

    assert response.status_code == 201
    assert response.json()["id"] not in {car["id"] for car in cars[:-1]}


def test_delete_missing_car_returns_404():
    response = client.delete("/cars/999")

    assert response.status_code == 404
