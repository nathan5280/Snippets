from typing import Dict

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.authenticate import authenticate, identity
from resources import Calculator
from auth import auth_db

TEST_USER_DB = "sqlite:///tests/db/test-users.db"


class CalculatorServer:
    def __init__(self, secret_key: str, cfg: Dict = None, test: bool = False):
        self.app = Flask(__name__)

        if cfg:
            self.app.config.update(cfg)

        self.app.secret_key = secret_key

        jwt = JWT(self.app, authenticate, identity)

        auth_db.init_app(self.app)

        self._api = Api(self.app)
        self._api.add_resource(Calculator, '/calculator/<string:operation>')

    def run(self):
        self.app.run(port=5000, debug=True)


if __name__ == '__main__':
    cfg = {
        "SQLALCHEMY_DATABASE_URI": TEST_USER_DB,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "PROPAGATE_EXCEPTIONS": True
    }

    calculator = CalculatorServer(secret_key="test", cfg=cfg)
    calculator.run()
