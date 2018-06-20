from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_model import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    full_name = Column(String(50))
    password = Column(String(12))

    # No cascading delete of addresses when their user is deleted.
    # addresses = relationship("Address", back_populates="user")

    # Cascading delete of addresses when user is deleted.
    addresses = relationship("Address", back_populates="user", cascade="all, delete, delete-orphan")

    equality_keys = ["name", "full_name", "password"]

    def __init__(self, *, name: str, full_name: str, password: str):
        self.name = name
        self.full_name = full_name
        self.password = password

    def __repr__(self):
        return f"User: id={self.id}, name={self.name}, full_name='{self.full_name}', password={self.password}"

    def __eq__(self, other):
        attr_equal = all([self.__dict__[k] == other.__dict__[k] for k in User.equality_keys])

        return attr_equal
