import pytest

from controller.exc import AlreadyExistsException, NotFoundException
from controller.session_scope import session_scope


def test_add_artist(library, first_artist):
    # given

    # execute
    with session_scope():
        library.artists.create(artist=first_artist)

        # expect
        artist_result = library.artists.read(name=first_artist.name)

        assert artist_result
        assert first_artist == artist_result


def test_add_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute / expect
    with pytest.raises(AlreadyExistsException) as e:
        with session_scope():
            library.artists.create(artist=first_artist)

    assert first_artist.name in str(e.value)


def test_read_existing_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist.name)

        # expect
        assert artist
        assert first_artist == artist


def test_read_nonexisting_artist(library, first_artist):
    # given

    # execute
    with pytest.raises(NotFoundException):
        with session_scope():
            artist = library.artists.read(name=first_artist.name)

            # expect
            assert not artist


def test_delete_artist_by_name(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist.name)
        library.artists.delete(name=first_artist.name)

        # expect
        with pytest.raises(NotFoundException) as e:
            artist = library.artists.read(name=first_artist.name)

        assert first_artist.name in str(e.value)


def test_delete_artist(library_one_artist, first_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artist = library.artists.read(name=first_artist.name)
        library.artists.delete(artist=artist)

        # expect
        with pytest.raises(NotFoundException):
            artist = library.artists.read(name=first_artist.name)


def test_delete_missing_artist(library, first_artist):
    # given

    # execute
    with pytest.raises(NotFoundException) as e:
        with session_scope():
            library.artists.delete(name=first_artist.name)

    assert first_artist.name in str(e.value)


def test_list_artist(library_one_artist):
    # given
    library = library_one_artist

    # execute
    with session_scope():
        artists_result = library.artists.list()

        # expect
        assert 1 == len(artists_result)
