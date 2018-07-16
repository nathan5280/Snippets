from models import InvalidContextError


class Stack:
    id_ = 0

    def __init__(self):
        self._stack = []
        Stack.id_ += 1

    def push(self, *, operand: float, id_: int) -> float:
        if Stack.id_ != id_:
            raise InvalidContextError()

        self._stack.append(operand)
        return operand

    def pop(self, *, id_: int) -> float:
        if Stack.id_ != id_:
            raise InvalidContextError()

        return self._stack.pop()

    def peek(self, *, id_: int) -> float:
        if Stack.id_ != id_:
            raise InvalidContextError

        return self._stack[-1]