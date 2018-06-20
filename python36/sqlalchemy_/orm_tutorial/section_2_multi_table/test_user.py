"""
Test the magic methods in User.
"""

from .user import User


def test_repr():
    # Given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")

    # Execute
    user_repr = str(user_1)

    # Expect
    expected_result = "User: id=None, name=ed, full_name='Edward Jones', password=eds-password"
    assert expected_result == user_repr


def test_eq_true():
    # Given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")
    user_2 = User(name="ed", full_name="Edward Jones", password="eds-password")

    # Execute

    # Expect
    assert user_1 == user_2


def test_eq_false():
    # Given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")
    user_2 = User(name="fred", full_name="Fredrick Jones", password="freds-password")

    # Execute

    # Expect
    assert not user_1 == user_2
