import pytest

from model.artist import Artist
from model.album import Album


def test_add_album(library_one_artist, first_artist, first_album):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute
    library.albums.create(artist_name=artist_name, album=album)

    # expect
    album_result = library.albums.read(artist_name=artist_name, name=first_album["name"])

    assert album_result
    assert album.name == album_result.name
    assert album.year == album_result.year


def test_add_existing_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist["name"]
    album = Album(name=first_album["name"], year=first_album["year"])

    # execute / expect
    with pytest.raises(ValueError):
        library.albums.create(artist_name=artist_name, album=album)


def test_read_existing_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist["name"]
    album_name = first_album["name"]

    # execute
    album_result = library.albums.read(artist_name=artist_name, name=album_name)

    # expect
    assert album_result
    assert album_name == album_result.name
    assert first_album["year"] == album_result.year


def test_read_nonexisting_album(library_one_artist, first_artist, first_album):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]
    album_name = first_album["name"]

    # execute
    album_result = library.albums.read(artist_name=artist_name, name=album_name)

    # except
    assert not album_result


def test_delete_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist["name"]
    album_name = first_album["name"]

    # execute
    library.albums.delete(artist_name=artist_name, name=album_name)

    # expect
    album_result = library.albums.read(artist_name=artist_name, name=album_name)

    assert not album_result


def test_list_album(library_one_artist_one_album, first_artist, first_album):
    # given
    library = library_one_artist_one_album
    artist_name = first_artist["name"]

    # execute
    albums_result = library.albums.list(artist_name=artist_name)

    # expect
    assert 1 == len(albums_result)