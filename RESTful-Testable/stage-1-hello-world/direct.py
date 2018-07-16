"""Run the model by direct function invocation."""

from models import AddCalculator, NumberType


def test_add(x: NumberType, y: NumberType) -> NumberType:
    # given
    calculator = AddCalculator()

    # when
    result = calculator.add(x=x, y=y)

    # then
    assert x + y == result

    return result


if __name__ == '__main__':
    result = test_add(1, 2)

    print(f"result={result}")
