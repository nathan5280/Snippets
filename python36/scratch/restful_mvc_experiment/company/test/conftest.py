import pytest

from sqla_conf import configure_direct_db, session
from library.controller import Company
from library.model import User


@pytest.fixture
def users():
    return [
        User(username="ed", email="ed@startup.com"),
        User(username="fred", email="fred@startup.com"),
        User(username="wendy", email="wendy@startu.com")
    ]


@pytest.fixture
def session_empty_db():
    """Return session for empty db."""
    configure_direct_db()

    return session()


@pytest.fixture
def session_pop_db(session_empty_db, users):
    """Return a session to a db that has the users populated in it."""
    for user in users:
        Company.users_create(session=session_empty_db, user=user)
    session_empty_db.commit()

    return session_empty_db
