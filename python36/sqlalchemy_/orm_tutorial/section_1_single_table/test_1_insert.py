from .user import User


def test_insert_one(empty_session):
    # given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")

    # execute
    empty_session.add(user_1)
    empty_session.commit()

    # expect
    user_result = empty_session.query(User).one()

    assert user_1 == user_result


def test_insert_list(empty_session):
    # given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")
    user_2 = User(name="fred", full_name="Fredrick Jones", password="freds-password")

    # execute
    empty_session.add_all([user_1, user_2])
    empty_session.commit()

    # expect
    user_result = empty_session.query(User).order_by(User.id).all()

    assert user_1 == user_result[0]
    assert user_2 == user_result[1]
