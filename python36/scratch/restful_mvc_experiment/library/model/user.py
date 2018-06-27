from sqla_conf import BaseClass
from sqlalchemy import Column, Integer, String


class User(BaseClass):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)

    _equality_keys = ["username", "email"]

    def __repr__(self):
        return f"<User {self.username}>"

    def __eq__(self, other):
        attr_equal = all([self.__dict__[k] == other.__dict__[k] for k in User._equality_keys])

        return attr_equal
