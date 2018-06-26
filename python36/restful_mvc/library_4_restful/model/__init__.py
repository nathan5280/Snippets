"""
Initialize the model declarative base for all model classes.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

print("Loading Model")

class DirectDB:
    _Session = None
    session = None

    @staticmethod
    def config_db(*, db_uri: str, echo: bool = False, create_db: bool = True) -> None:
        global _Session
        engine = create_engine(db_uri, echo=echo)

        if create_db:
            Base.metadata.create_all(engine)

        _Session = sessionmaker(bind=engine)

    @staticmethod
    def open_session():
        if DirectDB.session:
            return DirectDB.session

        DirectDB.session = _Session()
        return DirectDB.session

    @staticmethod
    def close_session():
        if DirectDB.session:
            DirectDB.session.close()
            DirectDB.session = None

