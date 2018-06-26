from typing import List, Union

from sqlalchemy.exc import IntegrityError

from controller.exc.already_exists_exception import AlreadyExistsException
from controller.exc.not_found_exception import NotFoundException
from model import DirectDB as Db
from model.album import Album
from model.artist import Artist


class Albums:
    @staticmethod
    def create(*, artist_name: str, album: Album) -> None:
        artist_working = Db.session.query(Artist).filter(Artist.name == artist_name).one_or_none()

        if not artist_working:
            raise NotFoundException(f"Artist '{artist_name}' not found in Library.")

        try:
            artist_working.albums.append(album)
            Db.session.commit()
        except IntegrityError:
            raise AlreadyExistsException(f"Artist '{artist_name}', Album '{album.name}' already exists in Library.'")

    @staticmethod
    def read(*, artist_name: str, name: str) -> Union[Album, None]:
        albums_result = (Db.session.query(Album).
                         join(Album.artist).
                         filter(Artist.name == artist_name).
                         filter(Album.name == name).
                         one_or_none()
                         )

        return albums_result

    @staticmethod
    def delete(*, artist_name: str, name: str) -> None:
        album = Albums.read(artist_name=artist_name, name=name)

        if album:
            Db.session.delete(album)

    @staticmethod
    def list(*, artist_name: str) -> List[Album]:
        albums_result = (Db.session.query(Album).
                         join(Album.artist).
                         filter(Artist.name == artist_name).
                         all()
                         )

        return albums_result
