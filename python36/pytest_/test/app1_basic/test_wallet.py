import pytest
from pytest_.app1_basic.wallet import Wallet
from pytest_.app1_basic.insufficient_amount_exception import InsufficientAmountException

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

"""
Test files names start with test_.  Test case names start with test_.  
This allows PyTest to find the test cases through introspection.
"""


def test_default_initial_amount(empty_wallet: Wallet)-> None:
    assert empty_wallet.balance == 0


def test_setting_inital_amount(wallet: Wallet)-> None:
    assert wallet.balance == 20


def test_wallet_add_cash(wallet: Wallet)-> None:
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet: Wallet)-> None:
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet: Wallet)-> None:
    with pytest.raises(InsufficientAmountException):
        wallet.spend_cash(100)


"""
Run a test multiple times with a set of parameters.
"""


@pytest.mark.parametrize('earned, spent, expected', [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(empty_wallet: Wallet, earned: float, spent: float, expected: float)-> None:
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


def test_millionaire(wallet_wealthy: Wallet)-> None:
    assert wallet_wealthy.balance == 1000000
