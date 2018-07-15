from typing import Union, Callable

NumberType = Union[int, float]


class RPN:
    """Simple RPN calculator built around an in memory stack."""
    stack = []

    @classmethod
    def clear(cls):
        """Clear the stack and start a new calculation."""
        cls.stack = []

    @classmethod
    def push(cls, number: NumberType) -> NumberType:
        """Push a number onto the stack."""
        cls.stack.append(number)
        return number

    @classmethod
    def binary_op(cls, operation: Callable) -> NumberType:
        """Apply the operation to the last two numbers on the stack."""
        x_operand = cls.stack.pop()
        y_operand = cls.stack.pop()
        result = operation(x_operand, y_operand)
        cls.stack.append(result)
        return result

    @classmethod
    def add(cls) -> NumberType:
        """Add the last two numbers on the stack."""
        result = cls.binary_op(lambda x, y: y + x)
        return result

    @classmethod
    def sub(cls) -> NumberType:
        """Subtract the last two numbers on the stack."""
        result = cls.binary_op(lambda x, y: y - x)
        return result
