import pytest
from flask import Flask
from flask.testing import FlaskClient

from library_app import LibraryApp


@pytest.fixture
def app() -> Flask:
    app = LibraryApp()

    return app.app


@pytest.fixture
def client(app: Flask) -> FlaskClient:

    return app.test_client()
