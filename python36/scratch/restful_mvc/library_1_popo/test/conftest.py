import pytest

from controller.library import Library
from model.album import Album
from model.artist import Artist
from test.data import test_data


@pytest.fixture
def data():
    return test_data


@pytest.fixture
def first_artist(data):
    artist = test_data[0]
    return artist


@pytest.fixture
def first_album(first_artist):
    album = first_artist["albums"][0]
    return album


@pytest.fixture()
def library():
    return Library()


@pytest.fixture
def library_one_artist(library, first_artist):
    artist = Artist(name=first_artist["name"])
    library.artists.create(artist=artist)

    return library


@pytest.fixture
def library_one_artist_one_album(library_one_artist, first_artist, first_album):
    album = Album(name=first_album["name"], year=first_album["year"])
    library_one_artist.albums.create(artist_name=first_artist["name"], album=album)

    return library_one_artist
