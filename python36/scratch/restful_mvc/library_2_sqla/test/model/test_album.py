from model.album import Album


def test_init():
    # given

    # execute
    album = Album(name="album", year=2000)

    # expect
    assert "album" == album.name
    assert 2000 == album.year
