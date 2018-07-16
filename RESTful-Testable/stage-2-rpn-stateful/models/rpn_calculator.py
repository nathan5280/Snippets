from typing import Callable

from models.stack import Stack
from models import OperandError


class RPNCalculator:
    """Simple RPN calculator built around an in memory stack."""
    stack = None

    @classmethod
    def start(cls):
        """Start a new calculation with a fresh stack."""
        cls.stack = Stack()
        return cls.stack.id_

    @classmethod
    def push(cls, operand: float, id_: int) -> float:
        """Push a number onto the stack."""
        pushed_operand = cls.stack.push(operand=operand, id_=id_)
        return pushed_operand

    @classmethod
    def binary_op(cls, *, operator: Callable, id_: int) -> float:
        """Apply the operation to the last two numbers on the stack."""
        try:
            x_operand = cls.stack.pop(id_=id_)
        except IndexError:
            raise OperandError("Stack empty.  Missing first operand.")

        try:
            y_operand = cls.stack.pop(id_=id_)
        except IndexError:
            raise OperandError("Stack empty.  Missing second operand.")

        result = operator(x_operand, y_operand)
        pushed_result = cls.stack.push(operand=result, id_=id_)
        return pushed_result

    @classmethod
    def add(cls, id_: int) -> float:
        """Add the last two numbers on the stack."""
        result = cls.binary_op(operator=lambda x, y: y + x, id_=id_)
        return result

    @classmethod
    def sub(cls, id_: int) -> float:
        """Subtract the last two numbers on the stack."""
        result = cls.binary_op(operator=lambda x, y: y - x, id_=id_)
        return result

    @classmethod
    def result(cls, id_: int) -> float:
        """Get the last entry in the stack."""
        try:
            result = cls.stack.peek(id_=id_)
            return result
        except IndexError:
            raise OperandError("Stack empty.")