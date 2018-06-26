from flask import Flask
from app import session, configure_flask_db
from library.model import User

print("app.py")


class Application:
    def __init__(self):
        self._app = Flask(__name__)

        configure_flask_db(app=self._app)

    def run(self):
        print("app.run()")

        admin = User(username="admin", email="admin@startup.com")

        session().add(admin)
        session().commit()

        user = session().query(User).one()
        print(user)
