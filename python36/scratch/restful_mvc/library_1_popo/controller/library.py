from typing import List, Union

from model.album import Album
from model.artist import Artist


class Library:
    class Artists:
        # Artists
        # Add/Create Artist
        # Get/Lookup Artist.name
        # Put/Update Artist (Skip for now. Albums only thing we can update and will do that through album interface.)
        # Delete Artist.name

        # List

        def __init__(self, library: 'Library'):
            self._library = library

        def create(self, *, artist: Artist) -> None:
            # Check for existing artist.
            artist_existing = self.read(name=artist.name)

            if artist_existing:
                raise ValueError(f"Artist: '{artist.name}' already exists in Library")

            self._library._artists.append(artist)

        def read(self, *, name: str) -> Union[Artist, None]:
            artists = list(filter(lambda artist: artist.name == name, self._library._artists))

            if not artists:
                return None

            return artists[0]

        def delete(self, *, name: str) -> None:
            self._library._artists = list(filter(lambda artist: artist.name != name, self._library._artists))

        def list(self) -> List[Artist]:
            return self._library._artists

    class Albums:
        # Albums
        # Add/Create Artist.name, Album
        # Get/Lookup Artist.name, Album
        # Put/Update Artist.name, Album (Hold off on this for now.)
        # Delete Artist.name, Album

        # List Artist.name

        # Get/Lookup Album.name

        def __init__(self, library: 'Library'):
            self._library = library

        def create(self, *, artist_name, album: Album) -> None:
            album_result = self.read(artist_name=artist_name, name=album.name)

            if album_result:
                raise ValueError(f"Artist: '{artist_name}', Album: '{album.name}' already exists in Library")

            artist = self._library.artists.read(name=artist_name)
            artist.albums.append(album)
            pass

        def read(self, *, artist_name: str, name: str) -> Union[Album, None]:
            artist_result = self._library.artists.read(name=artist_name)

            if not artist_result:
                raise ValueError(f"Artist: '{artist_name}' not found in Library")

            albums = list(filter(lambda album: name == name, artist_result.albums))

            if not albums:
                return None

            return albums[0]

        def delete(self, *, artist_name: str, name: str) -> None:
            artist_result = self._library.artists.read(name=artist_name)
            artist_result.albums = list(filter(lambda album: album.name != name, artist_result.albums))

        def list(self, *, artist_name: str) -> List[Album]:
            artist_result = self._library.artists.read(name=artist_name)
            return artist_result.albums

    def __init__(self):
        self._artists = []  # type: List[Artist]
        self.artists = Library.Artists(self)
        self.albums = Library.Albums(self)
