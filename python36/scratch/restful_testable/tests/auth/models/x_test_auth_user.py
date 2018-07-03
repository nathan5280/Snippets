from auth.models.user import User
from auth import auth_db


def test_create_user(db):
    # given
    name = "bob"
    password = "123"

    user = User(name=name, password=password)

    # execute
    user.save()

    # expect
    user_result = User.find(name=name)

    assert user_result
    assert name == user_result.name
    assert password == user_result.password


def test_find_user_name(user):
    # given
    # execute
    user_result = User.find(name=user.name)

    # expect
    assert user_result
    assert user.id == user_result.id
    assert user.name == user_result.name
    assert user.password == user_result.password


def test_find_user_id(user):
    # given
    # execute
    user_result = User.find(id_=user.id)

    # expect
    assert user_result
    assert user.id == user_result.id
    assert user.name == user_result.name
    assert user.password == user_result.password
