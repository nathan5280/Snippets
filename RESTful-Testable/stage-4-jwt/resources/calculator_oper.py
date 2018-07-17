from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models import RPNCalculator, InvalidContextError, OperandError


class CalculatorOper(Resource):
    """Resource wrapper to create a new Calculator"""
    parser = reqparse.RequestParser()
    parser.add_argument('operator',
                        type=str,
                        required=True,
                        help="Operation is required.")

    parser.add_argument('operand',
                        type=float,
                        required=False)

    @classmethod
    def put(cls, calc_id: int):
        """Request addition of the two numbers."""
        data = cls.parser.parse_args()

        operator = data['operator']
        if 'push' == operator:
            return {'result': RPNCalculator.push(id_=calc_id, operand=data['operand'])}, 200
        elif 'add' == operator:
            return {'result': RPNCalculator.add(id_=calc_id)}, 200
        elif 'sub' == operator:
            return {'result': RPNCalculator.sub(id_=calc_id)}, 200
        else:
            return {'message': f"Operation: {operator} not supported."}, 404

    @classmethod
    def get(cls, calc_id: int):
        """Get the last result."""
        try:
            result = RPNCalculator.result(id_=calc_id)
        except InvalidContextError:
            return {'message': "Invalid context."}, 400
        except OperandError:
            return {'message': "No result available."}, 400

        return {'result': result}

    @classmethod
    def delete(cls, calc_id: int):
        """Remove the Calculator"""
        RPNCalculator.delete(id_=calc_id)
