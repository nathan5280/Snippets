from sqlalchemy.orm.session import Session
from library.model import User


class Company:
    @staticmethod
    def users_create(*, session: _Session, user: User):
        session.add(user)

    @staticmethod
    def users_read(*, session: _Session, username: str):
        users = Company.users_list(session=session)
        user = session.query(User).filter(User.username == username).one()
        return user

    @staticmethod
    def users_list(*, session: _Session):
        users = session.query(User).order_by(User.id).all()
        return users

    @staticmethod
    def users_delete(*, session: _Session, username: str):
        user = Company.users_read(session=session, username=username)
        session.delete(user)
