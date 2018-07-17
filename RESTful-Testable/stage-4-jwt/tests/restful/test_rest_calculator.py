from flask.testing import FlaskClient
from auth import authorize


def test_auth() -> None:
    from server import CalculatorServer

    calculator = CalculatorServer()
    client = calculator.app.test_client()

    url = "auth"

    response = client.post(url, json={"username": "peter", "password": "123"})
    assert 200 == response.status_code
    auth_token =  response.get_json()["access_token"]

    url = '/calculator/v0'
    response = authorize(client.post, url, auth_token=auth_token, json={})
    assert 201 == response.status_code
    response_data = response.get_json()
    url = response_data['location']

    print(url)
    # assert False


def test_add_pass(client: FlaskClient, calc_url: str) -> None:
    # given
    x, y = 1, 2

    # when (add)
    client.put(calc_url, json={'operator': 'push', 'operand': x})
    client.put(calc_url, json={'operator': 'push', 'operand': y})
    client.put(calc_url, json={'operator': 'add'})

    # then
    # response = authorize(client.get, calc_url, auth_token=auth_token)
    response = client.get(calc_url)
    assert 200 == response.status_code
    response_data = response.get_json()
    assert x + y == response_data['result']


def test_sub_pass(client: FlaskClient, calc_url: str) -> None:
    # given
    x, y = 2, 1

    # when (sub)
    client.put(calc_url, json={'operator': 'push', 'operand': x})
    client.put(calc_url, json={'operator': 'push', 'operand': y})
    client.put(calc_url, json={'operator': 'sub'})

    # then
    response = client.get(calc_url)
    assert 200 == response.status_code
    response_data = response.get_json()
    assert x - y == response_data['result']


def test_close_pass(client: FlaskClient, calc_url: str) -> None:
    # given

    # when (close)
    client.delete(calc_url)

    # then (No calculator at the url)
    response = client.get(calc_url)
    assert 400 == response.status_code


def test_bad_operator_fail(client: FlaskClient, calc_url: str) -> None:
    # given

    # when (bad operator)
    response = client.put(calc_url, json={'operator': 'bad_oper'})

    # then
    assert 404 == response.status_code


def test_result_bad_context_fail(client: FlaskClient, calc_url: str) -> None:
    # given
    calc_url = calc_url + "0"

    # when (result, bad context)
    response = client.get(calc_url)

    # then (No calculator at the url)
    assert 400 == response.status_code


def test_result_no_operand_fail(client: FlaskClient, calc_url: str) -> None:
    # given

    # when (result, no operand)
    response = client.get(calc_url)

    # then
    assert 400 == response.status_code
