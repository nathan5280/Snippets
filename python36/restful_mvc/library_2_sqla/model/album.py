"""
SQLAlchemy enabled data object.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model import Base


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    year = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey("artists.id"))

    # Relationship albums -> artists
    artist = relationship("Artist", back_populates="albums")


if __name__ == '__main__':
    # a = Album()
    pass