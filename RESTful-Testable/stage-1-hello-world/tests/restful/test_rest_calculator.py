from flask.testing import FlaskClient


def test_add_pass(client: FlaskClient) -> None:
    """Test the AddCalculator RESTful API with the test client in the same process."""
    # given
    x, y = 1, 2
    request_data = {'x': x, 'y': y}
    url = '/calculator'

    # when (add)
    response = client.post(url, json=request_data)

    # then
    assert 200 == response.status_code

    response_data = response.get_json()
    assert x + y == response_data['result']
