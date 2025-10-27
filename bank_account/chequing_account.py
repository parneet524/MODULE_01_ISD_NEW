"""
chequing_account.py
-------------------
Subclass of BankAccount representing a chequing account.

Implements overdraft functionality and delegates service charge
calculation to the OverdraftStrategy class (Strategy Pattern).
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy


class ChequingAccount(BankAccount):
    """A chequing account with overdraft protection using the Strategy Pattern."""

    def __init__(self, account_number: int, client_number: int, balance, date_created,
                 overdraft_limit, overdraft_rate):
        """
        Initialize ChequingAccount using BankAccount attributes + subclass attributes.

        overdraft_limit:
            - Must be convertible to float.
            - Defaults to -100 if invalid.
        overdraft_rate:
            - Must be convertible to float.
            - Defaults to 0.05 (5%) if invalid.
        """
        # ---- call superclass initializer ----
        super().__init__(account_number, client_number, balance, date_created)

        # ---- validate overdraft_limit ----
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (TypeError, ValueError):
            self.__overdraft_limit = -100.0

        # ---- validate overdraft_rate ----
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (TypeError, ValueError):
            self.__overdraft_rate = 0.05

        # ---- assign the OverdraftStrategy ----
        self.__strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    # --------------------------------------------------------
    # __str__
    # --------------------------------------------------------
    def __str__(self) -> str:
        """Return formatted string showing account details per spec."""
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
            f"Account Type: Chequing"
        )

    # --------------------------------------------------------
    # get_service_charges
    # --------------------------------------------------------
    def get_service_charges(self) -> float:
        """
        Calculate and return service charges using the OverdraftStrategy.
        """
        return self.__strategy.calculate_service_charges(self)

