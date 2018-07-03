import requests


def main():
    response = requests.post("http://localhost:5000/auth", json={"username": "bob", "password": "123"})
    auth_token = response.json()["access_token"]

    a = 1
    b = 2
    resp = requests.get("http://localhost:5000/calculator/add", json={"a": 1, "b": 2}, headers={"JWT": auth_token})
    resp_data = resp.json()

    print(f"(a+b): a={a}, b={b}, result={resp_data['result']}")


if __name__ == '__main__':
    main()
