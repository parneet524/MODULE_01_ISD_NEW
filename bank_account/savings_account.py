"""
savings_account.py
------------------
This module defines the SavingsAccount class, which extends BankAccount.

A SavingsAccount is meant for clients with a short-term savings plan.
Typically, clients mainly deposit funds but may make occasional withdrawals.
"""
from datetime import date
from bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Represents a savings account within the banking system.
    Inherits from BankAccount and includes a minimum balance check.
    """

    SERVICE_CHARGE_PREMIUM = 2.0  # flat rate multiplier for below-minimum balances

    def __init__(self, account_number: int, client_number: int, balance, date_created: date, minimum_balance):
        """
        Initialize a new SavingsAccount instance.

        Args:
            account_number (int): Unique account number.
            client_number (int): Client number.
            balance (float): Starting balance.
            date_created (date): Account creation date.
            minimum_balance (float): Minimum balance before extra service charge applies.
        """
        # Initialize parent (BankAccount)
        super().__init__(account_number, client_number, balance, date_created)

        # Validate / assign minimum_balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except (TypeError, ValueError):
            self.__minimum_balance = 50.00

    @property
    def minimum_balance(self) -> float:
        """Return the minimum balance threshold."""
        return self.__minimum_balance

    def get_service_charges(self) -> float:
        """
        Calculate the service charge based on current balance and minimum balance.

        Returns:
            float: Calculated service charge.
        """
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self) -> str:
        """
        Return a formatted string representing the SavingsAccount.

        Format:
            Account Number: {account_number} Balance: ${balance:,.2f}
            Minimum Balance: ${minimum_balance:,.2f} Account Type: Savings
        """
        base_str = super().__str__()
        return f"{base_str}\nMinimum Balance: ${self.__minimum_balance:,.2f} Account Type: Savings"
