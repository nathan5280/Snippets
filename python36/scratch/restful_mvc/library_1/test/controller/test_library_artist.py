import pytest

from model.artist import Artist


def test_add_artist(library, first_artist):
    # given
    artist_name = first_artist["name"]
    artist = Artist(name=artist_name)

    # execute
    library.artists.create(artist=artist)

    # expect
    artist_result = library.artists.read(name=artist_name)

    assert artist_result
    assert artist.name == artist_result.name


def test_add_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]
    artist = Artist(name=artist_name)

    # execute / expect
    with pytest.raises(ValueError):
        library.artists.create(artist=artist)


def test_read_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]

    # execute
    artist = library.artists.read(name=artist_name)

    # expect
    assert artist
    assert artist_name == artist.name


def test_read_nonexisting_artist(library, first_artist):
    # given
    artist_name = first_artist["name"]

    # execute
    artist = library.artists.read(name=artist_name)

    # expect
    assert not artist


def test_delete_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]

    # execute
    library.artists.delete(name=artist_name)

    # expect
    artist = library.artists.read(name=artist_name)
    assert not artist


def test_list_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist
    artist_name = first_artist["name"]

    # execute
    artists_result = library.artists.list()

    # expect
    assert 1 == len(artists_result)

