from typing import List, Union

from model.album import Album as AlbumModel
from model.artist import Artist as ArtistModel


class Albums:
    @staticmethod
    def create(*, album: AlbumModel, artist: ArtistModel = None, artist_name: str = None) -> None:
        assert artist or artist_name

        if not artist:
            artist = ArtistModel.read(name=artist_name)

        artist.albums.append(album)
        album.save()

    @staticmethod
    def read(*, artist_name: str, name: str) -> Union[AlbumModel, None]:
        album = AlbumModel.read(artist_name=artist_name, name=name)

        return album

    @staticmethod
    def delete(*, artist_name: str, name: str) -> None:
        album = Albums.read(artist_name=artist_name, name=name)
        album.delete()

    @staticmethod
    def list() -> List[AlbumModel]:
        return AlbumModel.list()
