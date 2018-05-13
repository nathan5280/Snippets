from pytest_.app1_basic.insufficient_amount_exception import InsufficientAmountException


class Wallet(object):
    """
    Simple class used to demonstrate the use of PyTest.
    """

    def __init__(self, initial_amount: float = 0) -> None:
        """
        Initialize the wallet with a initial amount of money.

        :param initial_amount: Initial amount of money in the wallet.
        """
        self._balance = initial_amount

    def spend_cash(self, amount: float) -> None:
        """
        Spend money and deduct it from the current amount of money in the wallet.

        :param amount: Amount of money being spent.
        :return: None

        Raises: Insufficient funds exception when the balance in the wallet is less than the amount being spent..
        """
        if self._balance < amount:
            raise InsufficientAmountException('Not enough available to spend {}.'.format(amount))
        self._balance -= amount

    def add_cash(self, amount: float) -> None:
        """
        Add the specified amount to the balance in the wallet.

        :param amount:  Amount to add to the wallet's balance.
        :return: None
        """
        self._balance += amount

    @property
    def balance(self) -> float:
        """
        Return the current balance of the wallet.
        :return: Balance currently in the wallet.
        """
        return self._balance
