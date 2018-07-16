import pytest

from models import AddCalculator


@pytest.fixture
def calculator() -> AddCalculator:
    """Instantiate a AddCalculator model as a test fixture for the individual test cases."""
    add_calculator = AddCalculator()
    return add_calculator
