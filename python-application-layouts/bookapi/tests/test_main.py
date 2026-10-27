from fastapi.testclient import TestClient

from bookapi.main import app

client = TestClient(app)


def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "A Wizard of Earthsea"


def test_read_missing_author():
    response = client.get("/authors/99")
    assert response.status_code == 404


def test_admin_requires_token():
    assert (
        client.post("/admin/", headers={"X-Token": "wrong"}).status_code == 400
    )
    response = client.post(
        "/admin/", headers={"X-Token": "fake-super-secret-token"}
    )
    assert response.status_code == 200
