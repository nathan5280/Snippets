from model.album import Album


def test_init(first_album):
    # given

    # execute
    album = Album(**first_album)

    # expect
    assert first_album["name"] == album.name
    assert first_album["year"] == album.year
