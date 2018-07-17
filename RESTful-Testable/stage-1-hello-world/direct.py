"""Run the model by direct function invocation."""

from models import AddCalculator


def test_add(x: float, y: float) -> float:
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
