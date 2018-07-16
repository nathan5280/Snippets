from collections import namedtuple
import pytest
from models import RPNCalculator

ModelDataClass = namedtuple('ModelData', ('calc', 'calc_id'))


@pytest.fixture
def model() -> ModelDataClass:
    calc = RPNCalculator()
    calc_id = calc.start()

    return ModelDataClass(calc, calc_id)
