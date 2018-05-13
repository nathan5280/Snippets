import requests
import json


def case1():
    r = requests.get('https://api.github.com/events')
    print(r)


def case2():
    # Parameters are easily encoded in the URL from a dictionary.
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://httpbin.org/get', params=payload)
    print(r.url)


def case3():
    # List as a parameter.
    payload = {'key1': 'value1', 'key2': ['value2 1', 'value2.2']}
    r = requests.get('http://httpbin.org/get', params=payload)
    print(r.url)


def case4():
    # Accessing information from the response.
    r = requests.get('https://api.github.com/events')
    print(r.encoding)
    print(r.text)


def case5():
    # Accessing JSON
    r = requests.get('http://api.github.com/events')
    print(r.json()[0])


def case6():
    # Headers are added as a dictionary.
    url = 'https://api.github.com/events'
    headers = {'user-agent': 'my-app1_basic/0.0.1'}
    r = requests.get(url, headers=headers)


def case7():
    # Adding and encoding form data
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=payload)
    print(r.text)


def case8_1():
    # Passing parameters directly.  No encoding is done by requets
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1'}
    r = requests.post(url, data=json.dumps(payload))
    print(r.text)

def case8_2():
    # Automatically passing the json representation of the data.
    url = 'http://httpbin.org/post'
    payload = {'key1': 'value1'}
    r = requests.post(url, json=payload)
    print(r.text)


def case9():
    # Check the status code.
    # Parameters are easily encoded in the URL from a dictionary.
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('http://httpbin.org/get', params=payload)
    print(r.status_code)

    r = requests.get('http://httpbin.org/status/404', params=payload)
    print(r.status_code)



if __name__ == '__main__':
    # case1()
    # case2()
    # case3()
    # case4()
    # case5()
    # case6()
    # case7()
    # case8_1()
    # case8_2()
    case9()