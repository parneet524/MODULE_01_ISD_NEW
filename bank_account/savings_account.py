# bank_account/savings_account.py
"""
Defines the SavingsAccount class which uses the MinimumBalanceStrategy
to calculate service charges.
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):
    """Represents a savings account using the Strategy Pattern."""

    def __init__(self, account_number: int, client_number: int, balance: float,
             date_created, minimum_balance: float):
        """
        Initialize SavingsAccount using BankAccount attributes + subclass attributes.

        :param minimum_balance: The minimum balance requirement for this account.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # validate minimum balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except (TypeError, ValueError):
            self.__minimum_balance = 50.00

        # assign MinimumBalanceStrategy
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)


    def get_service_charges(self) -> float:
        """Calculate and return service charges using the MinimumBalanceStrategy."""
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return formatted string showing account details."""
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Minimum Balance: ${self.__strategy._minimum_balance:,.2f} "
            f"Account Type: Savings"
        )
