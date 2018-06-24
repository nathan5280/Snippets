import pytest

from model.artist import Artist
from controller.session_scope import session_scope
from controller.already_exists_exception import AlreadyExistsException


def test_add_artist(library, first_artist):
    # given
    artist = Artist(name=first_artist["name"])

    # execute
    with session_scope():
        library.artists.create(artist=artist)

        # expect
        artist_result = library.artists.read(name=first_artist["name"])

        assert artist_result
        assert first_artist["name"] == artist_result.name


def test_add_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist
    artist = Artist(name=first_artist["name"])

    # execute / expect
    with pytest.raises(AlreadyExistsException) as e:
        with session_scope():
            library.artists.create(artist=artist)

            assert first_artist["name"] in str(e.value)


def test_read_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist["name"])

        # expect
        assert artist
        assert first_artist["name"] == artist.name


def test_read_nonexisting_artist(library, first_artist):
    # given

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist["name"])

        # expect
        assert not artist


def test_delete_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        library.artists.delete(name=first_artist["name"])

        # expect
        artist = library.artists.read(name=first_artist["name"])
        assert not artist


def test_list_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artists_result = library.artists.list()

        # expect
        assert 1 == len(artists_result)

