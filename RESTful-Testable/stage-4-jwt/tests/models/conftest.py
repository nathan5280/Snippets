from collections import namedtuple
import pytest
from models import RPNCalculator
from models.db import create_db

ModelDataClass = namedtuple('ModelData', ('calc', 'calc_id'))


@pytest.fixture
def model() -> ModelDataClass:
    """Create a new calculator and start a new calculation."""
    create_db(connection_string = 'sqlite:///:memory:')
    calc = RPNCalculator()
    calc_id = calc.start()

    return ModelDataClass(calc, calc_id)
