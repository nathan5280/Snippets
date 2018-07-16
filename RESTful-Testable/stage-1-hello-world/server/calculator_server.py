from flask import Flask
from flask_restful import Api

from resources import Calculator


class CalculatorServer:
    """RESTful API server for the calculator."""
    def __init__(self):
        self.app = Flask(__name__)
        self._api = Api(self.app)

        # Expose the single add endpoint.
        self._api.add_resource(Calculator, '/calculator')

    def run(self):
        self.app.run(port=5000, debug=True)
