from typing import Union

NumType = Union[int, float]


class Calculator:
    @staticmethod
    def add(*, a: NumType, b: NumType) -> NumType:
        return a + b
