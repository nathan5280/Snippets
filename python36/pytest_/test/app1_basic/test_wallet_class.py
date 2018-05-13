import pytest
from pytest_.app1_basic.wallet import Wallet

"""
PyTest Fixtures are a simple way to extract boiler plate code that is used in several different test cases
into a single location.  Think of it as setup code for objects that your test cases need to execute.
"""


@pytest.fixture
def empty_wallet():
    """
    Returns a Wallet instance with a zero balance
    """
    return Wallet()


@pytest.fixture
def wallet():
    """
    Returns a Wallet instance with a balance of 20
    """
    return Wallet(20)


class TestWalletClass:
    """
    Test cases can be organized and collected into classes.
    """

    def test_default_initial_amount(self, empty_wallet):
        assert empty_wallet.balance == 0

    def test_setting_inital_amount(self, wallet):
        assert wallet.balance == 20

