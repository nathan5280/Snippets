"""
SQLAlchemy Configurator to help bridge between the differences in sqlalchemy and flask_sqlalchemy
to allow testing of the model and RESTfull API with no application code changes.

Model classes that use SQLAlchemy used different base classes in the two different models.
- SQLAlchemy derives from the BaseClass returned by sqlalchemy.ext.declarative()
- Flask-SQLAlchemy derives from flask_sqlalchemy.SQLAlchemy

Sessions are also accessed through different mechanisms.
- SQLAlchemy accesses everything through the rich SQLAlchemy object.
- Flask-SQLAlchemy accesses the session through the sqlalchemy.orm.sessionmaker method.

This module hides these differences allowing for applications to be developed in a modular and
testable way for each of the different implementation models and separate concerns.

The module is configured through a simple configuration file in the modules directory.
Switching the mode field in the configuration file selects how sqlalchemy is configured.

Mode:
    Flask: Configure for flask_sqlalchemy and RESTful API
    Direct: Configure for sqlalchemy and directly accessing the model/controller.

Production:
    True: Use the configuration parameters from [flask|direct]_prod.
    False: Use the configuration parameters from [flask|direct]_test.
"""
import json

# ToDo: Pull the configuration path from somewhere other than the code.  Environment variable?
with open("sqla_conf/cfg.json", 'rt') as fp:
    cfg = json.load(fp)

BaseClass = None
db = None
engine = None
app_session = None


if "Flask" == cfg["mode"]:
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()

    BaseClass = db.Model

elif "Direct" == cfg["mode"]:
    from sqlalchemy.ext.declarative import declarative_base

    BaseClass = declarative_base()

else:
    raise ValueError(f"Module app configuration mode: {cfg['mode']} is invalid.  Use (Flask | Direct).")


def configure_flask_db(*, app):
    cfg_key = "".join(["flask_", "prod" if cfg["production"] else "test"])
    app.config.from_mapping(cfg[cfg_key])
    app.app_context().push()

    db.init_app(app)
    db.create_all()

    def get_flask_session():
        return db.session

    global app_session
    app_session = get_flask_session


def configure_direct_db():
    from sqlalchemy import create_engine

    cfg_key = "".join(["flask_", "prod" if cfg["production"] else "test"])
    engine = create_engine(cfg[cfg_key]["SQLALCHEMY_DATABASE_URI"])

    from sqlalchemy.orm import sessionmaker

    BaseClass.metadata.create_all(engine)

    global app_session
    app_session = sessionmaker(engine)


def session():
    return app_session()

