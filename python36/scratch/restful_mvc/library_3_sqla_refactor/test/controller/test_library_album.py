import pytest

from controller.exc import AlreadyExistsException, NotFoundException
from controller.session_scope import session_scope
from model.album import Album


def test_add_album_artist_name(library_one_artist, first_artist, first_album):
    # given
    library = library_one_artist
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute
    with session_scope():
        library.albums.create(artist_name=first_artist.name, album=album)

        # expect
        album_result = library.albums.read(artist_name=first_artist.name, name=first_album["name"])

        assert album_result
        assert album.name == album_result.name
        assert album.year == album_result.year


def test_add_album_artist(library_one_artist, first_artist, first_album):
    # given
    library = library_one_artist
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist.name)
        library.albums.create(artist=artist, album=album)

        # expect
        album_result = library.albums.read(artist_name=first_artist.name, name=first_album["name"])

        assert album_result
        assert album.name == album_result.name
        assert album.year == album_result.year


def test_add_existing_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute / expect
    with pytest.raises(AlreadyExistsException):
        with session_scope():
            library.albums.create(artist_name=first_artist.name, album=album)


def test_add_existing_album_artist(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute / expect
    with pytest.raises(AlreadyExistsException):
        with session_scope():
            library.albums.create(artist=first_artist, album=album)


def test_add_misssing_album(library, first_artist, first_album):
    # given
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute / expect
    with pytest.raises(NotFoundException):
        with session_scope():
            library.albums.create(artist_name=first_artist.name, album=album)


def test_read_existing_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist.name
    album_name = first_album["name"]

    # execute
    with session_scope():
        album_result = library.albums.read(artist_name=artist_name, name=album_name)

        # expect
        assert album_result
        assert album_name == album_result.name
        assert first_album["year"] == album_result.year


def test_read_nonexisting_album(library_one_artist, first_artist, first_album):
    # given
    library = library_one_artist
    artist_name = first_artist.name
    album_name = first_album["name"]

    # execute
    with session_scope():
        album_result = library.albums.read(artist_name=artist_name, name=album_name)

        # except
        assert not album_result


def test_delete_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist.name
    album_name = first_album["name"]

    # execute
    with session_scope():
        library.albums.delete(artist_name=artist_name, name=album_name)

        # expect
        album_result = library.albums.read(artist_name=artist_name, name=album_name)

        assert not album_result


def test_list_album(library_one_artist_one_album, first_artist):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist.name

    # execute
    with session_scope():
        albums = library.albums.list()

        # expect
        assert 1 == len(albums)
