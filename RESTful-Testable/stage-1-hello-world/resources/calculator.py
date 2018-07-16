from flask_restful import Resource, reqparse

from models import AddCalculator


class Calculator(Resource):
    """Resource wrapper around the AddCalculator Class"""
    parser = reqparse.RequestParser()
    parser.add_argument('x',
                        type=float,
                        required=True,
                        help="First operand is required.")

    parser.add_argument('y',
                        type=float,
                        required=True,
                        help="Second operand is required.")

    @classmethod
    def post(cls):
        """Request addition of the two numbers."""
        data = cls.parser.parse_args()

        result = AddCalculator.add(**data)
        return {"result": result}, 200
