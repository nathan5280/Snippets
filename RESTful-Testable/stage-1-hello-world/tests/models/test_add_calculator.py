from models import AddCalculator


def test_add_pass():
    """
    Test the AddCalculator model directly.
    """
    # given
    x, y = 1, 2

    # when (add numbers)
    result = AddCalculator.add(x=x, y=y)

    # then
    assert x + y == result
