"""Client to invoke the add function in the Calculator Server through the RESTful API"""

import requests
from models import NumberType


def test_add(x: NumberType, y: NumberType) -> NumberType:
    # given
    url = 'http://localhost:5000/calculator'
    data = {'x': x, 'y': y}

    # when (Request add)
    response = requests.post(url, json=data)

    # then
    assert 200 == response.status_code

    response_data = response.json()
    assert x + y == response_data['result']

    return response_data['result']


if __name__ == '__main__':
    result = test_add(1, 2)
    print(f'result={result}')