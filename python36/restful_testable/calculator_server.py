from flask import Flask
from flask_restful import Api

from resources import Calculator


class CalculatorServer:
    def __init__(self):
        self.app = Flask(__name__)
        self._api = Api(self.app)

        self._api.add_resource(Calculator, '/calculator/<string:operation>')

    def run(self):
        self.app.run(port=5000, debug=True)


if __name__ == '__main__':
    calculator = CalculatorServer()
    calculator.run()
