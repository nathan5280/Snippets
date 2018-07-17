import pytest

from auth.user import User

_user = User(username="peter", id_=1, password="123")


def test_find_by_username_pass():
    # given
    # when
    user = User.find(username=_user.username)

    # then
    assert user
    assert _user == user


def test_find_by_id_pass():
    # given
    # when
    user = User.find(id_=_user.id)

    # then
    assert user
    assert _user == user


def test_missing_user_pass():
    # given
    bad_id = -1

    # when
    user = User.find(id_=bad_id)

    # then
    assert not user


def test_overlapping_args_fail():
    # given
    # when
    # then
    with pytest.raises(AssertionError):
        User.find(username=_user.username, id_=_user.id)


def test_no_args_fail():
    # given
    # then
    with pytest.raises(AssertionError):
        User.find()
