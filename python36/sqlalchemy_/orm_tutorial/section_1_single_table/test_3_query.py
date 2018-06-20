from .user import User


def test_query_all(three_session, users):
    # given

    # execute
    user_result = three_session.query(User).order_by(User.id).all()

    # expect
    for i, user in enumerate(users):
        assert user == user_result[i]


def test_query_all_tuple(three_session, users):
    # given

    # execute
    result = three_session.query(User.name, User.full_name)

    # expect
    i = 0
    for name, full_name in result:
        assert users[i].name == name
        assert users[i].full_name == full_name
        i += 1


def test_query_all_keyed_tuple(three_session, users):
    # given

    # execute
    result = three_session.query(User.name, User.full_name)

    # expect
    for i, user_row in enumerate(result):
        assert users[i].name == user_row.name
        assert users[i].full_name == user_row.full_name

