from .user import User
from .address import Address

def test_cascading_delete(user_with_addresses_session):
    # given

    # execute
    user = user_with_addresses_session.query(User).one()

    # expect
    assert 2 == len(user.addresses)

    # execute
    user_with_addresses_session.delete(user)
    count = user_with_addresses_session.query(Address).count()

    # expect
    assert 0 == count