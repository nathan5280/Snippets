from flask.testing import FlaskClient


def test_add(client: FlaskClient) -> None:
    # given
    a = 1
    b = 2

    req_data = {"a": a, "b": b}
    url = f"/calculator/add"

    # execute
    resp = client.get(url, json=req_data)

    # expect
    assert 200 == resp.status_code
    resp_data = resp.get_json()

    assert a + b == float(resp_data["result"])
