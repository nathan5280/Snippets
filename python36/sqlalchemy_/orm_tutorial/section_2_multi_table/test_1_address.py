from .user import User


def test_no_address(one_session):
    # given

    # execute
    user_result = one_session.query(User).filter(User.name == "ed").one()

    # expect
    assert 0 == len(user_result.addresses)


def test_add_address(one_session, addresses):
    # given
    user = one_session.query(User).filter(User.name == "ed").one()
    user.addresses = addresses
    one_session.commit()

    # execute
    user = one_session.query(User).filter(User.name == "ed").one()

    # expect
    for i, address in enumerate(addresses):
        assert address.email_address == user.addresses[i].email_address

    # Check that the address points back to the user.
    assert "ed" == user.addresses[0].user.name
