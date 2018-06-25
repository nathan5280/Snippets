from contextlib import contextmanager

from model import DirectDB


@contextmanager
def session_scope():
    """Consistent session scope around a set of operations."""
    session = DirectDB.open_session()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        DirectDB.close_session()
