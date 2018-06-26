import pytest

from model import DirectDB as DB
from model.artist import Artist
from model.album import Album
from controller.library import Library
from controller.session_scope import session_scope
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


@pytest.fixture
def db():
    DB.config_db(db_uri="sqlite:///:memory:", echo=False, create_db=True)


@pytest.fixture()
def library(db):
    return Library()


@pytest.fixture
def library_one_artist(library, first_artist):
    artist = Artist(name=first_artist["name"])

    with session_scope():
        library.artists.create(artist=artist)

    return library


@pytest.fixture
def library_one_artist_one_album(library_one_artist, first_artist, first_album):
    album = Album(name=first_album["name"], year=first_album["year"])

    with session_scope():
        library_one_artist.albums.create(artist_name=first_artist["name"], album=album)

    return library_one_artist
