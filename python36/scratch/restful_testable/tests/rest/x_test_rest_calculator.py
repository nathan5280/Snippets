from flask.testing import FlaskClient
from auth.authorize_wrapper import authorize


def test_add(client: FlaskClient, auth_token: str) -> None:
    # given
    a = 1
    b = 2

    req_data = {"a": a, "b": b}
    url = f"/calculator/add"

    # execute
    resp = authorize(client.get, url, auth_token=auth_token, json=req_data)

    # expect
    assert 200 == resp.status_code
    resp_data = resp.get_json()

    assert a + b == float(resp_data["result"])
