import pytest
from flask import Flask
from flask.testing import FlaskClient

from controller.exc import AlreadyExistsException, NotFoundException
from controller.session_scope import session_scope


def test_add_artist(library, first_artist, client):
    # given
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.post(url)

    # expect
    assert 200 == response.status_code
    response = client.get(url)

    assert 200 == response.status_code
    artist_data = response.get_json()
    assert first_artist.name == artist_data["name"]


def test_add_existing_artist(library_one_artist, first_artist, client):
    # given
    library = library_one_artist
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.post(url)

    # expect
    assert 500 == response.status_code
    response_data = response.get_json()
    assert first_artist.name in response_data["message"]


def test_read_existing_artist(library_one_artist, first_artist, client):
    # given
    library = library_one_artist
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.get(url)

    # expect
    assert 200 == response.status_code
    artist_data = response.get_json()
    assert first_artist.name == artist_data["name"]


def test_read_nonexisting_artist(library, first_artist, client):
    # given
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.get(url)

    # expect
    assert 404 == response.status_code
    response_data = response.get_json()
    assert first_artist.name in str(response_data["message"])


def test_delete_artist_by_name(library_one_artist, first_artist, client):
    # given
    library = library_one_artist
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.delete(url)

    # expect
    assert 200 == response.status_code

    # Check that the artist was deleted.
    artist_result = client.get(url)
    assert 404 == artist_result.status_code


def test_delete_missing_artist(library, first_artist, client):
    # given
    url = f"/library/artists/{first_artist.name}"

    # execute
    response = client.delete(url)

    # expect
    assert 500 == response.status_code


def test_list_artist(library_all, client):
    # given
    url = f"/library/artists"

    # execute
    response = client.get(url)

    # expect
    resp_data = response.get_json()
    assert 3 == len(resp_data["artists"])