from typing import List, Union

from sqlalchemy.exc import IntegrityError

from controller.already_exists_exception import AlreadyExistsException
from controller.not_found_exception import NotFoundException
from model import DirectDB as DB
from model.album import Album
from model.artist import Artist


class Albums:
    # Albums
    # Add/Create Artist.name, Album
    # Get/Lookup Artist.name, Album
    # Put/Update Artist.name, Album (Hold off on this for now.)
    # Delete Artist.name, Album

    # List Artist.name

    # Get/Lookup Album.name

    @staticmethod
    def create(*, artist_name: str, album: Album) -> None:
        # ToDo: Decide if Albums should know about library to get access to Artists.
        # This will require all of the static methods to become instance methods with self.
        # There will also need to be an __init__ method.  This also applies to Artists.
        artist_working = DB.session.query(Artist).filter(Artist.name == artist_name).one()
        if not artist_working:
            raise NotFoundException(f"Artist '{aritst_name}' not found in Library.")

        try:
            artist_working.albums.append(album)
            DB.session.commit()
        except IntegrityError:
            raise AlreadyExistsException(f"Artist '{artist_name}', Album '{album.name}' already exists in Library.'")

    @staticmethod
    def read(*, artist_name: str, name: str) -> Union[Album, None]:
        albums_result = (DB.session.query(Album).
                         join(Album.artist).
                         filter(Artist.name == artist_name).
                         filter(Album.name == name).
                         one_or_none()
                         )

        return albums_result

    @staticmethod
    def delete(*, artist: Artist, name: str) -> None:
        DB.session.delete(artist)

    def list(self, *, artist: Artist) -> List[Album]:
        albums_result = (DB.session.query(Album).
                         join(Album.artist).
                         filter(Artist.name == artist.name).
                         all()
                         )

        return albums_result
