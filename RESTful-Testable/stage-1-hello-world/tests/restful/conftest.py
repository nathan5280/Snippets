import pytest
from flask.testing import FlaskClient

from server import CalculatorServer


@pytest.fixture
def client() -> FlaskClient:
    """Get a test client for the AddCalculator RESTful API server."""
    calculator = CalculatorServer()
    return calculator.app.test_client()
