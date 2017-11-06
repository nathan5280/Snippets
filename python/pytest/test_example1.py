# PyTest example
from .example1 import func

pass_tests = True


def test_answer():
    if pass_tests:
        assert func(3) == 4
    else:
        assert func(3) == 5
