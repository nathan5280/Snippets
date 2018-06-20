from .address import Address
from .user import User


def test_with_addresses(user_with_addresses_session, addresses):
    # given

    # execute
    user = user_with_addresses_session.query(User).filter(User.name == "ed").one()

    # expect
    for i, address in enumerate(addresses):
        assert address.email_address == user.addresses[i].email_address

    # Check that the address points back to the user.
    assert "ed" == user.addresses[0].user.name


def test_implicit_join(user_with_addresses_session):
    # given

    # execute
    result = (user_with_addresses_session.query(User, Address).
              filter(User.id == Address.user_id).all()
              )

    # expect
    assert 2 == len(result)


def test_explicit_join(user_with_addresses_session):
    # given

    # execute
    # find the user that has the email address ed@google.com
    user = (user_with_addresses_session.query(User).join(Address).
            filter(Address.email_address == "ed@google.com").one()
            )

    # expect
    assert "ed" == user.name


def test_alias_table_self_join(user_with_addresses_session):
    from sqlalchemy.orm import aliased
    # given

    # execute
    address_alias1 = aliased(Address)
    address_alias2 = aliased(Address)

    user, email1, email2 = (
        user_with_addresses_session.query(User.name, address_alias1.email_address, address_alias2.email_address).
        join(address_alias1, User.addresses).
        join(address_alias2, User.addresses).
        filter(address_alias1.email_address == "ed@google.com").
        filter(address_alias2.email_address == "edward@startup.com").one()
        )

    # expect
    assert "ed" == user
    assert "ed@google.com" == email1
    assert "edward@startup.com" == email2