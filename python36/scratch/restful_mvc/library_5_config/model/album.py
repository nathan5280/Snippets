"""
SQLAlchemy enabled data object.
"""
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from controller.exc import AlreadyExistsException, NotFoundException
from model import Base
from model import DirectDB as Db
from model.artist import Artist


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    year = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey("artists.id"))

    # Relationship albums -> artists
    artist = relationship("Artist", back_populates="albums")

    equality_keys = ["name", "year"]

    def save(self) -> None:
        try:
            Db.session.add(self)
            Db.session.commit()
        except IntegrityError as e:
            raise AlreadyExistsException(f"Album '{self.name}' already exists in Library.")

    @classmethod
    def read(cls, *, artist_name: str, name: str) -> 'Artist':
        albums_result = (Db.session.query(cls).
                         join(cls.artist).
                         filter(Artist.name == artist_name).
                         filter(cls.name == name).
                         one_or_none()
                         )

        return albums_result

    def update(self) -> None:
        Db.session.commit()

    def delete(self) -> None:
        Db.session.delete(self)
        Db.session.commit()

    @classmethod
    def list(cls) -> List['Album']:
        return Db.session.query(cls).all()

    def json(self):
        return {
            "name": self.name,
            "year": self.year
        }

    def __eq__(self, obj):
        equal = all([getattr(self, k) == getattr(obj, k) for k in self.equality_keys])

        return equal
