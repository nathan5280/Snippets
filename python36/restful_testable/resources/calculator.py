from flask import request
from flask_restful import Resource

from models import Calculator as CalculatorModel


class Calculator(Resource):
    @staticmethod
    def get(operation):
        req_data = request.get_json()

        if "add" == operation:
            result = CalculatorModel.add(**req_data)
            return {"result": result}, 200
