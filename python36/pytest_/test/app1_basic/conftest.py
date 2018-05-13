import pytest

from pytest_.app1_basic.wallet import Wallet

@pytest.fixture
def wallet_wealthy():
    """
    Returns a Wallet instance with a balance of 20
    """
    return Wallet(1000000)


