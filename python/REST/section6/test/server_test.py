import requests
import json
import pytest_
import os


@pytest_.fixture()
def host():
    """Valid host for tests"""
    return 'http://localhost:5000'


@pytest_.yield_fixture(autouse=True)
def clear_db(host):
    end_point_url = '/'.join((host, 'clear'))
    r = requests.delete(end_point_url)
    assert r.status_code == 200


def test_register_first_time(host):
    end_point_url = '/'.join((host, 'register'))
    payload = {'username': 'bob', 'password': 'xyz'}
    r = requests.post(end_point_url, json=payload)
    assert r.status_code == 201


def test_register_second_time(host):
    end_point_url = '/'.join((host, 'register'))
    payload = {'username': 'bob', 'password': 'xyz'}
    r = requests.post(end_point_url, json=payload)
    assert r.status_code == 201

    r = requests.post(end_point_url, json=payload)
    assert r.status_code == 400


def test_add_store(host):
    end_point_url = '/'.join((host, 'store', 'Store 1'))
    r = requests.post(end_point_url)
    assert r.status_code == 200