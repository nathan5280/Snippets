from .user import User


def test_count(three_session):
    # given

    # execute
    count = three_session.query(User).filter(User.name.like("%ed")).count()

    # expect
    assert 2 == count
