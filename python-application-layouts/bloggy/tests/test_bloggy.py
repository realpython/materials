from bloggy.db import get_db


def test_index_without_posts(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"No posts yet." in response.data


def test_index_lists_posts(app, client):
    with app.app_context():
        db = get_db()
        db.execute(
            "INSERT INTO post (title, body) VALUES (?, ?)",
            ("Hello, Flask", "My first post."),
        )
        db.commit()
    assert b"Hello, Flask" in client.get("/").data


def test_login_page(client):
    response = client.get("/auth/login")
    assert response.status_code == 200
    assert b"<h1>Log In</h1>" in response.data
