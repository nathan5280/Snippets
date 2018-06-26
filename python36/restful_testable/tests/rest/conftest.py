import pytest
from flask import Flask
from flask.testing import FlaskClient

from calculator_server import CalculatorServer


@pytest.fixture
def app() -> Flask:
    app = CalculatorServer()
    return app.app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
