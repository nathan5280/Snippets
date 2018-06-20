import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base_model import Base
from .user import User
from .address import Address

Session = None


@pytest.fixture
def users():
    return [
        User(name="ed", full_name="Edward Jones", password="eds-password"),
        User(name="fred", full_name="Fredrick Jones", password="freds-password"),
        User(name="wendy", full_name="Wendy Washington", password="wendys-password")
    ]


@pytest.fixture
def first_user(users):
    return users[0]


@pytest.fixture
def empty_session():
    """Return session for empty db."""
    engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)

    session = Session()
    return session


@pytest.fixture
def one_session(empty_session, first_user):
    """Return session for db with one users."""
    empty_session.add(first_user)
    empty_session.commit()

    return empty_session


@pytest.fixture
def three_session(empty_session, users):
    """Return session for populated db."""
    empty_session.add_all(users)
    empty_session.commit()

    return empty_session


@pytest.fixture
def addresses():
    return [
        Address(email_address="ed@google.com"),
        Address(email_address="edward@startup.com")
    ]


@pytest.fixture
def user_with_addresses_session(empty_session, first_user, addresses):
    first_user.addresses = addresses
    empty_session.add(first_user)
    empty_session.commit()

    return empty_session
