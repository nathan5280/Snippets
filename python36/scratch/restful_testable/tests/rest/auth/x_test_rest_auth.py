from flask.testing import FlaskClient

def test_add_user(client: FlaskClient) -> None:
    # given
    username = "bob1"
    password = 456

    req_data = {
        "username": username,
        "password": password
    }

    url = f"/users/username"

    # execute
    result = client.post(url, json=req_data)