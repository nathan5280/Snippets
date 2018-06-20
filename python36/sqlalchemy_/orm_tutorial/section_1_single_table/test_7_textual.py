from sqlalchemy import text

from .user import User


def test_textual_comparison(three_session, first_user):
    # given

    # execute
    user_result = (three_session.query(User).
                   filter(text("id<2")).one()
                   )

    # expect
    assert first_user.name == user_result.name


def test_textual_parameters(three_session, first_user):
    # given

    # execute
    user_result = (three_session.query(User).
                   filter(text("id<:id_value and name=:name_value")).
                   params(id_value=2, name_value='ed').one()
                   )

    # expect
    assert first_user.name == user_result.name


def text_textual_select_1(three_session, first_user):
    # given

    # execute
    user_result = (three_session.query(User).from_statement(
        text("SELECT * FROM users where name=:name").
        params(name="ed").one())
    )

    # expect
    assert first_user.name == user_result.name


def text_textual_select_2(three_session, first_user):
    # given
    stmt = text("SELECT * FROM users where name=:name")
    stmt = stmt.columns(User.name, User.id)

    # execute
    user_result = three_session.query(stmt).params(name="ed").one()

    # expect
    assert first_user.name == user_result.name


def text_textual_select_3(three_session, first_user):
    # given
    stmt = text("SELECT name, id FROM users where name=:name")

    # execute
    user_result = three_session.query(stmt).params(name="ed").one()

    # expect
    assert first_user.name == user_result.name
