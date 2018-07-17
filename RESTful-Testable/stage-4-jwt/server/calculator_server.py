from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.authenticate import authenticate, identity
from resources import Calculator, CalculatorOper
from models import RPNCalculator
from models.db import create_db


class CalculatorServer:
    """RESTful API server for the calculator."""

    def __init__(self):
        self.app = Flask(__name__)

        # This should come from somewhere external in production.
        self.app.secret_key = "secret_key"
        JWT(self.app, authenticate, identity)

        # Create the RPNCalculator.  This should handle if the DB is created fresh or reused.
        # RPNCalculator()
        create_db(connection_string='sqlite:///:memory:')

        self._api = Api(self.app)
        # Expose the calculator endpoint.
        # Request a new calculator be created.
        self._api.add_resource(Calculator, '/calculator/v0')

        # Access the operations on the calculator based on the calculator location url return when
        # the calculator was requested.  (push, add, sub, result, delete)
        self._api.add_resource(CalculatorOper, '/calculator/v0/<int:calc_id>')

    # def run(self):
    #     self.app.run(port=5000, debug=True)
