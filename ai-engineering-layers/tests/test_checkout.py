import pytest

from app.api import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(str(tmp_path / "orders.db"))
    return app.test_client()


def test_checkout_creates_order(client):
    response = client.post("/checkout", json={"item": "widget", "quantity": 1})
    assert response.status_code == 201


def test_checkout_totals_the_quantity(client):
    response = client.post("/checkout", json={"item": "widget", "quantity": 3})
    assert response.get_json()["total"] == 13.5


def test_unknown_item_is_rejected(client):
    response = client.post("/checkout", json={"item": "nope", "quantity": 1})
    assert response.status_code == 400


def test_orders_endpoint_lists_orders(client):
    client.post("/checkout", json={"item": "gadget", "quantity": 2})
    response = client.get("/orders")
    assert response.status_code == 200
    assert response.get_json()[0]["item"] == "gadget"


def test_order_ids_increment(client):
    first = client.post("/checkout", json={"item": "widget", "quantity": 1})
    second = client.post("/checkout", json={"item": "widget", "quantity": 1})
    assert second.get_json()["id"] == first.get_json()["id"] + 1
