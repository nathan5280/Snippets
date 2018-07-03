import pytest
from flask import Flask
from flask.testing import FlaskClient

from calculator_server import CalculatorServer


TEST_USER_DB = "sqlite:///tests/db/test-users.db"


@pytest.fixture
def app() -> Flask:
    cfg = {
        "SQLALCHEMY_DATABASE_URI": TEST_USER_DB,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "PROPAGATE_EXCEPTIONS": True
    }

    app = CalculatorServer(secret_key="test", cfg=cfg)
    return app.app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def auth_token(client: FlaskClient):
    url = "auth"

    response = client.post(url, json={"username": "bob", "password": "123"})
    assert 200 == response.status_code
    return response.get_json()["access_token"]
