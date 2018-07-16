from models import InvalidContextError


class Stack:
    """Simple in memory stack for RPN calculator."""
    id_ = 0     # ID to keep track of stacks and calculations.

    def __init__(self):
        """Initialize a new stack with a new unique ID."""
        self._stack = []
        Stack.id_ += 1

    def push(self, *, operand: float, id_: int) -> float:
        """Push a new operand onto the stack."""
        if Stack.id_ != id_:
            raise InvalidContextError()

        self._stack.append(operand)
        return operand

    def pop(self, *, id_: int) -> float:
        """Pop an operand of the stack."""
        if Stack.id_ != id_:
            raise InvalidContextError()

        return self._stack.pop()

    def peek(self, *, id_: int) -> float:
        """Peek at the top operand in the stack."""
        if Stack.id_ != id_:
            raise InvalidContextError

        return self._stack[-1]