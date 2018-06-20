from .user import User
from sqlalchemy.orm import aliased


def test_col_label(one_session, first_user):
    # given

    # execute
    user_result = one_session.query(User.name.label('name_label')).one()

    # expect
    assert first_user.name == user_result.name_label


def test_table_alias(one_session, first_user):
    # given
    user_alias = aliased(User, name="user_alias")

    # execute
    # user_result = one_session.query(user_table_alias, user_table_alias.name).order_by(user_table_alias.id).one()
    user_result = one_session.query(user_alias, user_alias.name).one()

    # expect
    assert first_user == user_result.user_alias
