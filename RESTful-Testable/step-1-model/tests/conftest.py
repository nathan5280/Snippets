from models.rpn import RPN
import pytest


@pytest.fixture
def calculator():
    calc = RPN()
    calc.clear()
    return calc
