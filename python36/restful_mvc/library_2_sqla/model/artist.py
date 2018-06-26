"""
SQLAlchemy enabled data object.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model import Base


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)

    # Relationship artists -> albums with cascading delete if artist is removed.
    albums = relationship("Album", back_populates="artist", cascade="all, delete, delete-orphan")

    equality_keys = ["name"]

    def __eq__(self, other):
        attr_equal = all(self.__dict__[k] == other.__dict__[k] for k in self.equality_keys)

        return attr_equal