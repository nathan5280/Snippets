import pytest
from flask.testing import FlaskClient

from auth import authorize
from server import CalculatorServer


@pytest.fixture
def client() -> FlaskClient:
    """Get a test client for the AddCalculator RESTful API server."""
    calculator = CalculatorServer()
    return calculator.app.test_client()


@pytest.fixture
def auth_token(client: FlaskClient):
    url = "auth"

    response = client.post(url, json={"username": "peter", "password": "123"})
    assert 200 == response.status_code
    return response.get_json()["access_token"]


@pytest.fixture
def calc_url(client: FlaskClient, auth_token):
    """Request a new calculator be created."""
    url = '/calculator/v0'
    response = authorize(client.post, url, auth_token=auth_token)
    assert 201 == response.status_code
    response_data = response.get_json()
    url = response_data['location']

    return url


# Note that PyTest is smart enough to only call the client test fixture once for each test
# even though the test takes it as an argument and the cacl_url takes it as an argument.
