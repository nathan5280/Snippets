from models import AddCalculator


def test_add_pass(calculator: AddCalculator):
    """
    Test the AddCalculator model directly.
    """
    # given
    x, y = 1, 2

    # when (add numbers)
    result = calculator.add(x=x, y=y)

    # then
    assert x + y == result
