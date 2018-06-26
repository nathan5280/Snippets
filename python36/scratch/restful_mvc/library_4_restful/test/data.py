from controller.library import Library
from controller.session_scope import session_scope

from model.artist import Artist
from model.album import Album

test_data = [
    {
        "name": "U2",
        "albums": [
         {
                "name": "War",
                "year": 1983
            },
            {
                "name": "The Joshua Tree",
                "year": 1987
            },
            {
                "name": "Rattle and Hum",
                "year": 1988
            }
        ]
    },
    {
        "name": "The Rolling Stones",
        "albums": [
            {
                "name": "Sticky Fingers",
                "year": 1971
            },
            {
                "name": "Goats Head Soup",
                "year": 1973
            },
            {
                "name": "Tattoo You",
                "year": 1981
            }
        ]
    },
    {
        "name": "Junior Brown",
        "albums": [
            {
                "name": "Semi Crazy",
                "year": 1996
            },
            {
                "name": "Long Walk Back",
                "year": 1998
            },
            {
                "name": "Down Home Chrome",
                "year": 2004
            }
        ]
    }
]


def populate_db():
    with session_scope():
        for artist_data in test_data:
            artist = Artist(name=artist_data["name"])

            for album_data in artist_data["albums"]:
                album = Album(**album_data)
                artist.albums.append(album)

            artist.save()



