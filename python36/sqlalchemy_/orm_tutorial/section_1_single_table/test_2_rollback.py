from .user import User


def test_rollback(empty_session):
    # given
    user_1 = User(name="ed", full_name="Edward Jones", password="eds-password")

    empty_session.add(user_1)
    empty_session.commit()

    # execute
    # Change the state of the objects in the session.
    user_1.name = "Bob"

    user_fake = User(name='fakeuser', full_name="nobody", password="11111")
    empty_session.add(user_fake)

    # expect
    # Check to see what the session knows.
    users = empty_session.query(User).order_by(User.id).all()
    assert 2 == len(users)
    assert user_1 == users[0]
    assert user_fake == users[1]

    # execute
    empty_session.rollback()
    user = empty_session.query(User).one()

    # expect
    assert user_1 == user
