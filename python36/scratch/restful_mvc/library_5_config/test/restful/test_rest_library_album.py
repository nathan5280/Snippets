import pytest
from flask import Flask
from flask.testing import FlaskClient

from controller.exc import AlreadyExistsException, NotFoundException
from controller.session_scope import session_scope


def test_add_album_artist_name(library_one_artist, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.post(url, json={"year": first_album.year})

    # expect
    assert 201 == response.status_code
    resp_data = response.get_json()
    assert first_album.name == resp_data["name"]
    assert first_album.year == resp_data["year"]

    # Query the library to make sure the album was added.
    response = client.get(url)
    assert 200 == response.status_code
    resp_data = response.get_json()
    assert first_album.name == resp_data["name"]
    assert first_album.year == resp_data["year"]


def test_add_existing_album(library_one_artist_one_album, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.post(url, json={"year": first_album.year})

    # expect
    assert 500 == response.status_code


def test_add_misssing_album(library, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.post(url, json={"year": first_album.year})

    # expect
    assert 500 == response.status_code


def test_read_existing_album(library_one_artist_one_album, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.get(url)

    # expect
    assert 200 == response.status_code
    resp_data = response.get_json()
    assert first_album.name == resp_data["name"]
    assert first_album.year == resp_data["year"]


def test_read_nonexisting_album(library_one_artist, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.get(url)

    # expect
    assert 404 == response.status_code
    resp_data = response.get_json()
    assert first_artist.name in resp_data["message"]
    assert first_album.name in resp_data["message"]


def test_update_album(library_one_artist_one_album, first_artist, first_album, client):
    # given
    first_album.year += 100
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.put(url, json={"year": first_album.year})

    # expect
    assert 201 == response.status_code

    # Query the library to make sure the album was added.
    response = client.get(url)
    assert 200 == response.status_code
    resp_data = response.get_json()
    assert first_album.name == resp_data["name"]
    assert first_album.year == resp_data["year"]


def test_update_missing_album(library_one_artist, first_artist, first_album, client):
    # given
    first_album.year += 100
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.put(url, json={"year": first_album.year})

    # expect
    assert 404 == response.status_code


def test_delete_album(library_one_artist_one_album, first_artist, first_album, client):
    # given
    url = f"/library/albums/{first_artist.name}/{first_album.name}"

    # execute
    response = client.delete(url)

    # expect
    assert 200 == response.status_code


def test_list_artist(library_all, client):
    # given
    url = f"/library/albums"

    # execute
    response = client.get(url)

    # expect
    resp_data = response.get_json()
    assert 9 == len(resp_data["albums"])