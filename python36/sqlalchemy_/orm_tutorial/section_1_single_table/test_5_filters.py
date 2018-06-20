from .user import User


def test_slicing(three_session, users):
    # given

    # execute
    user_result = three_session.query(User).order_by(User.id)[1:2]

    # expect
    for i, user in enumerate(users[1:2]):
        assert user == user_result[i]


def test_filter_by(three_session, first_user):
    # given
    filter_full_name = first_user.full_name

    # execute
    # SQL like comparision
    user_result = three_session.query(User).filter_by(full_name=filter_full_name).one()

    # expect
    assert first_user == user_result


def test_filter(three_session, first_user):
    # given
    filter_full_name = first_user.full_name

    # execute
    # Python like comparision
    user_result = three_session.query(User).filter(User.full_name == filter_full_name).one()

    # expect
    assert first_user == user_result


def test_filter_filter(three_session, first_user):
    # given
    filter_name = first_user.name
    filter_full_name = first_user.full_name

    # execute
    # Python like comparision
    user_result = (three_session.query(User).
                   filter(User.name == filter_name).
                   filter(User.full_name == filter_full_name).one()
                   )

    # Prefer the use of the () to encapsulate the multiline statement.
    # In the below version of it a space after one of the \ blows it all up.
    # user_result = three_session.query(User).\
    #     filter(User.name==filter_name).\
    #     filter(User.full_name==filter_full_name).one()

    # expect
    assert first_user == user_result


def test_filters(three_session):
    # Equals
    three_session.query(User).filter(User.name == "ed").one()

    # not equals
    user_result = three_session.query(User).filter(User.name != "ed").all()
    assert 2 == len(user_result)

    # like
    user_result = three_session.query(User).filter(User.name.like("%ed")).all()
    assert 2 == len(user_result)

    # ilike (Case insensitive like)
    user_result = three_session.query(User).filter(User.name.ilike("%ED")).all()
    assert 2 == len(user_result)

    # in
    user_result = three_session.query(User).filter(User.name.in_(["ed", "fred"])).all()
    assert 2 == len(user_result)

    # not in
    three_session.query(User).filter(~User.name.in_(["ed", "fred"])).one()

    # null
    user_result = three_session.query(User).filter(User.name == None).all()
    assert 0 == len(user_result)

    user_result = three_session.query(User).filter(User.name.is_(None)).all()
    assert 0 == len(user_result)

    # not null
    user_result = three_session.query(User).filter(User.name != None).all()
    assert 3 == len(user_result)

    user_result = three_session.query(User).filter(User.name.isnot(None)).all()
    assert 3 == len(user_result)

    # and
    from sqlalchemy import and_
    three_session.query(User).filter(and_(User.name == "ed", User.full_name == "Edward Jones")).one()
    three_session.query(User).filter(User.name == "ed", User.full_name == "Edward Jones").one()
    three_session.query(User).filter(User.name == "ed").filter(User.full_name == "Edward Jones").one()

    # or
    from sqlalchemy import or_
    user_result = three_session.query(User).filter(or_(User.name == "ed", User.name == "wendy")).all()
    assert 2 == len(user_result)

    # match
    # Not supported on sqlite
    from sqlalchemy.exc import OperationalError
    try:
        three_session.query(User).filter(User.name.match("ed")).all()
    except OperationalError as e:
        pass

