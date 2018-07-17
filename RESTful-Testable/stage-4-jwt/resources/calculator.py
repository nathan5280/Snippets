from flask_jwt import jwt_required
from flask_restful import Resource

from models import RPNCalculator


class Calculator(Resource):
    """Resource wrapper to create a new Calculator"""

    @classmethod
    @jwt_required()
    def post(cls):
        """Request a new calculator."""
        id_ = RPNCalculator.start()

        url = f"/calculator/v0/{id_}"
        return {"location": url}, 201
