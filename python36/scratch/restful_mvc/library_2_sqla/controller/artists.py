from typing import List, Union

from sqlalchemy.exc import IntegrityError

from controller.already_exists_exception import AlreadyExistsException
from model import DirectDB as DB
from model.artist import Artist


class Artists:
    # Artists
    # Add/Create Artist
    # Get/Lookup Artist.name
    # Put/Update Artist (Skip for now. Albums only thing we can update and will do that through album interface.)
    # Delete Artist.name

    # List

    @staticmethod
    def create(*, artist: Artist) -> None:
        try:
            DB.session.add(artist)
            DB.session.commit()
        except IntegrityError as e:
            raise AlreadyExistsException(f"Artist '{artist.name}' already exists in Library.")

    @staticmethod
    def read(*, name: str) -> Union[Artist, None]:
        artists_result = DB.session.query(Artist).filter(Artist.name == name).one_or_none()

        return artists_result

    @staticmethod
    def delete(*, name: str) -> None:
        artist = Artists.read(name=name)

        if artist:
            DB.session.delete(artist)

    @staticmethod
    def list() -> List[Artist]:
        artists_result = DB.session.query(Artist).all()

        return artists_result
