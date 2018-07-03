from models import Calculator


def test_add():
    # given
    a = 1
    b = 2

    # execute
    r = Calculator.add(a=a, b=b)

    # expect
    assert r == a + b
