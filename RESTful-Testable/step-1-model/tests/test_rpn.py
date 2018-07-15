import pytest

from models.rpn import RPN


def test_values_add_success(calculator: RPN):
    # given
    x = 1
    y = 2

    # when (add)
    calculator.push(x)
    calculator.push(y)
    r = calculator.add()

    # then
    assert x + y == r


def test_values_multiple_add_success(calculator: RPN):
    # given
    x = 1
    y = 2
    z = 3

    # when (add)
    calculator.push(x)
    calculator.push(y)
    calculator.add()
    calculator.push(z)
    r = calculator.add()

    # then
    assert x + y + z == r


def test_values_multiple_push_add_success(calculator: RPN):
    # given
    x = 1
    y = 2
    z = 3

    # when (add)
    calculator.push(x)
    calculator.push(y)
    calculator.push(z)
    calculator.add()
    r = calculator.add()

    # then
    assert x + y + z == r


def test_values_sub_success(calculator: RPN):
    # given
    x = 3
    y = 2

    # when (add)
    calculator.push(x)
    calculator.push(y)
    r = calculator.sub()

    # then
    assert x - y == r


def test_values_multiple_sub_success(calculator: RPN):
    # given
    x = 3
    y = 2
    z = 1

    # when (add)
    calculator.push(x)
    calculator.push(y)
    calculator.sub()
    calculator.push(z)
    r = calculator.sub()

    # then
    assert x - y - z == r


def test_values_multiple_push_sub_success(calculator: RPN):
    # given
    x = 3
    y = 2
    z = 1

    # when (add)
    calculator.push(x)
    calculator.push(y)
    calculator.push(z)
    r = calculator.sub()
    r = calculator.sub()

    # then
    assert (x - (y - z)) == r


def test_value_add_missing_operand_fail(calculator: RPN):
    # given
    x = 1

    # when (add - only one operand)
    calculator.push(x)
    with pytest.raises(IndexError):
        r = calculator.add()
