import pytest

from bloggy import create_app
from bloggy.db import init_db


@pytest.fixture
def app(tmp_path):
    app = create_app(
        {"TESTING": True, "DATABASE": str(tmp_path / "test.sqlite")}
    )
    with app.app_context():
        init_db()
    return app


@pytest.fixture
def client(app):
    return app.test_client()
