from library.controller import Company


def test_insert_user(session_empty_db, users):
    session = session_empty_db

    # given

    # execute
    Company.users_create(session=session, user=users[0])
    session.commit()

    # expect
    user_result = Company.users_read(session=session, username=users[0].username)

    assert users[0] == user_result


def test_list_users(session_pop_db, users):
    session = session_pop_db

    # given

    # execute
    users_result = Company.users_list(session=session)

    # expect
    for i, user in enumerate(users_result):
        assert users[i] == user


def test_delete_user(session_pop_db, users):
    session = session_pop_db

    # given

    # execute
    Company.users_delete(session=session, username=users[0].username)
    session.commit()

    # expect
    users_result = Company.users_list(session=session)
    assert 2 == len(users_result)