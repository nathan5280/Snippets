from controller.session_scope import session_scope


def test_add_existing_artist(library_all):
    # given
    library = library_all

    # execute
    with session_scope():
        artists = library.artists.list()

        # excpect
        assert 3 == len(artists)


def test_stress_list(library_all):
    # given
    library = library_all

    # execute
    with session_scope():
        artists = library.artists.list()

        # excpect
        assert 3 == len(artists)

        artists = library.artists.list()

        # excpect
        assert 3 == len(artists)

    with session_scope():
        artists = library.artists.list()

        # excpect
        assert 3 == len(artists)

        artists = library.artists.list()

        # excpect
        assert 3 == len(artists)
