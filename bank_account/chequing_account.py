"""
chequing_account.py
-------------------
Subclass of BankAccount representing a chequing account.

Implements overdraft functionality and its own get_service_charges().
"""

from bank_account.bank_account import BankAccount


class ChequingAccount(BankAccount):
    """A chequing account with overdraft protection and service charge rules."""

    def __init__(self, account_number: int, client_number: int, balance, date_created, overdraft_limit, overdraft_rate):
        """
        Initialize ChequingAccount using BankAccount attributes + subclass attributes.

        overdraft_limit:
            - Must be convertible to float.
            - Default to -100 if invalid.
        overdraft_rate:
            - Must be convertible to float.
            - Default to 0.05 (5%) if invalid.
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

    # --------------------------------------------------------
    # __str__
    # --------------------------------------------------------
    def __str__(self) -> str:
        """
        Return string showing account details formatted per spec.

        Example:
        Account Number: 1234567 Balance: $1,559.49
        Overdraft Limit: $-15.00 Overdraft Rate: 5.00% Account Type: Chequing
        """
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
        Calculate and return service charges based on overdraft status.

        Formula:
            If balance >= overdraft_limit:
                service = BASE_SERVICE_CHARGE
            Else:
                service = BASE_SERVICE_CHARGE + (overdraft_limit - balance) * overdraft_rate
        """
        balance = self.balance

        if balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - balance) * self.__overdraft_rate
