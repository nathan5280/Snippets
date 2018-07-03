import os

import pytest

from auth import auth_db
from calculator_server import CalculatorServer

from auth.models.user import User


@pytest.fixture
def db():
    cfg = {
        # "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_DATABASE_URI": "sqlite:////tmp/test.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }

    app = CalculatorServer(secret_key="test", cfg=cfg)
    app.app.app_context().push()

    # auth_db.session.expire_all()
    auth_db.drop_all()
    auth_db.create_all()



@pytest.fixture
def user(db):
    name = "bob"
    password = "123"

    new_user = User(name=name, password=password)
    new_user.save()

    return new_user
