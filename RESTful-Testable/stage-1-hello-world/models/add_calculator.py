from models import NumberType


class AddCalculator:
    """Simple calculator that can add two numbers together."""

    @staticmethod
    def add(*, x: NumberType, y: NumberType) -> NumberType:
        """Add two numbers and return result."""
        return x + y
