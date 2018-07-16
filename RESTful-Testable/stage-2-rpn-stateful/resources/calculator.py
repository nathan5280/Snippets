from flask_restful import Resource, reqparse, request
from models import RPNCalculator


class Calculator(Resource):
    """Resource wrapper to create a new Calculator"""

    calculator = RPNCalculator()

    @classmethod
    def post(cls):
        """Request a new calculator."""
        id_ = cls.calculator.start()

        url = f"/calculator/v0/{id_}"
        return {"location": url}, 201
