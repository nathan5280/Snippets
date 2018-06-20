from .user import User


def test_list_all(three_session):
    # given

    # execute
    user_result = three_session.query(User).all()

    # expect
    assert 3 == len(user_result)


def test_list_first(three_session):
    # given

    # execute
    user_result_all = three_session.query(User).all()
    user_result_first = three_session.query(User).first()

    # expect
    assert 3 == len(user_result_all)
    assert User is type(user_result_first)


def test_list_one_true(three_session):
    # given

    # execute
    user_result = three_session.query(User).filter(User.name == "ed").one()

    # expect
    assert User is type(user_result)


def test_list_one_error(three_session):
    # given

    # execute
    from sqlalchemy.orm.exc import NoResultFound
    try:
        user_result = three_session.query(User).filter(User.name.like == ("%ed")).one()
    except NoResultFound:
        pass

    # expect


def test_list_one_or_none_none(three_session):
    # given

    # execute
    user_result = three_session.query(User).filter(User.name == "Bob").one_or_none()

    # expect
    assert None is user_result


def test_list_one_or_none_one(three_session):
    # given

    # execute
    user_result = three_session.query(User).filter(User.name == "ed").one_or_none()

    # expect
    assert User is type(user_result)