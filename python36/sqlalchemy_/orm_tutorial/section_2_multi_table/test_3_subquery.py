from .user import User
from .address import Address


def test_with_addresses(three_session, addresses):
    """
    Join for a count of email addresses per user.

    SELECT users.*, adr_count.address_count FROM users LEFT OUTER JOIN
    (SELECT user_id, count(*) AS address_count
        FROM addresses GROUP BY user_id) AS adr_count
    ON users.id=adr_count.user_id
    """
    # given
    from sqlalchemy.sql import func

    user = three_session.query(User).first()
    user.addresses = addresses
    three_session.commit()

    stmt = (three_session.query(Address.user_id, func.count('*').
                                label("address_count")).
            group_by(Address.user_id).subquery()
            )

    # execute
    result = (three_session.query(User, stmt.c.address_count).
              outerjoin(stmt, User.id == stmt.c.user_id).order_by(User.id)
              )


    # expect
    # for r in result:
    #     print(r.User, r.address_count)

    assert 2 == result[0].address_count
    # Not sure why this None instead of 0
    assert None is result[1].address_count
