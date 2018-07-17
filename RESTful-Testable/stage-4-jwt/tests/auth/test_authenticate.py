from auth.authenticate import authenticate, identity
from auth.user import User

_user = User(username="peter", id_=1, password="123")


def test_authenticate_pass():
    # given
    # when
    user = authenticate(username=_user.username, password=_user.password)

    # then
    assert _user == user


def test_identify_pass():
    # given
    # when
    user = identity(payload={'identity': 1})

    # then
    assert _user == user


def test_authenticate_fail():
    # given
    bad_password = "bad_pwd"

    # when
    user = authenticate(username=_user.username, password=bad_password)

    # then
    assert None is user


def test_identify_fail():
    # given
    bad_id = -1

    # when
    user = identity(payload={'identity': bad_id})

    # then
    assert None is user
