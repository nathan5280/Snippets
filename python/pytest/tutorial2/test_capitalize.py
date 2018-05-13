# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
import pytest_


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('x must be a string.')
    return x.capitalize()


def test_capital_case1():
    # input is lower
    assert capital_case('all lower') == 'All lower'


def test_capital_case2():
    # input is already capitalized.
    assert capital_case('All lower') == 'All lower'


def test_wrong_type():
    # Check for passing something other than a string.
    with pytest_.raises(TypeError):
        capital_case(1)
