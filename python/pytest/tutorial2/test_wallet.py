import pytest_
from wallet import Wallet, InsufficientAmount


@pytest_.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest_.fixture
def wallet():
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_inital_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet):
    with pytest_.raises(InsufficientAmount):
        wallet.spend_cash(100)


@pytest_.mark.parametrize('earned, spent, expected', [
    (30, 10, 20),
    (20, 2, 18)
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
