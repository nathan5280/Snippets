from typing import List, Union

from model.artist import Artist as ArtistModel


class Artists:
    @staticmethod
    def create(*, artist: ArtistModel) -> None:
        artist.save()

    @staticmethod
    def read(*, name: str) -> Union[ArtistModel, None]:
        return ArtistModel.read(name=name)

    @staticmethod
    def delete(*, artist: ArtistModel=None, name: str=None) -> None:
        assert artist or name

        if not artist:
            artist = ArtistModel.read(name=name)

        artist.delete()

    @staticmethod
    def list() -> List[ArtistModel]:
        return ArtistModel.list()
