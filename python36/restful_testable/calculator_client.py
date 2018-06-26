import requests


def main():
    a = 1
    b = 2
    resp = requests.get("http://localhost:5000/calculator/add", json={"a": 1, "b": 2})
    resp_data = resp.json()

    print(f"(a+b): a={a}, b={b}, result={resp_data['result']}")


if __name__ == '__main__':
    main()
