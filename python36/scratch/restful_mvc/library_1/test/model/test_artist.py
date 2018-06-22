from model.album import Album
from model.artist import Artist


def test_init(first_artist):
    # given
    albums = []
    for album in first_artist["albums"]:
        albums.append(Album(**album))

    artist_name = first_artist["name"]

    # execute
    artist = Artist(name=artist_name, albums=albums)

    # expect
    assert artist_name == artist.name
    assert len(first_artist["albums"]) == len(artist.albums)


def test_no_albums_init(data):
    """Check to make sure that two different empty artists don't have the same list of albums."""
    # given
    artist_name_1 = data[0]["name"]
    artist_name_2 = data[1]["name"]

    # execute
    artist_1 = Artist(name=artist_name_1)
    artist_2 = Artist(name=artist_name_2)

    # expect
    assert artist_1.albums is not artist_2.albums

    artist_1.albums.append(Album(name="abc", year=2000))
    assert 1 == len(artist_1.albums)
    assert 0 == len(artist_2.albums)