from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

AppDBBase = declarative_base()
_session_maker = None


def create_db(*, connection_string: str):
    engine = create_engine(connection_string, echo=False)
    AppDBBase.metadata.create_all(engine)

    global _session_maker
    _session_maker = sessionmaker(engine)


@contextmanager
def session_scope() -> Session:
    """Provide transactional scope around a series of operations."""
    session = _session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
