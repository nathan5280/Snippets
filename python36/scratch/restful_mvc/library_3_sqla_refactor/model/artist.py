"""
SQLAlchemy enabled data object.
"""
from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from controller.exc import AlreadyExistsException, NotFoundException
from model import Base
from model import DirectDB as Db


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)

    # Relationship artists -> albums with cascading delete if artist is removed.
    albums = relationship("Album", back_populates="artist", cascade="all, delete, delete-orphan")

    equality_keys = ["name"]

    @classmethod
    def read(cls, *, name: str) -> 'Artist':
        try:
            artist = Db.session.query(cls).filter(cls.name == name).one()
        except NoResultFound:
            raise NotFoundException(f"Artist '{name}' not found in Library")

        return artist

    def save(self) -> None:
        try:
            Db.session.add(self)
            Db.session.commit()
        except IntegrityError as e:
            raise AlreadyExistsException(f"Artist '{self.name}' already exists in Library.")

    def delete(self) -> None:
        Db.session.delete(self)
        Db.session.commit()

    @classmethod
    def list(cls) -> List['Artist']:
        artists = Db.session.query(cls).all()

        return artists

    def __eq__(self, obj):
        equal = all([getattr(self, k) == getattr(obj, k) for k in self.equality_keys])

        return equal
