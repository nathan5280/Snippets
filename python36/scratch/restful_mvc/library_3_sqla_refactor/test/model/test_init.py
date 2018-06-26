from model import DirectDB as Db
from controller.session_scope import session_scope


def test_session():
    Db.config_db(db_uri="sqlite:///:memory:", echo=False, create_db=True)

    with session_scope():
        session_outer_id = id(Db.session)

        with session_scope():
            session_inner_id = id(Db.session)

        assert session_outer_id == session_inner_id