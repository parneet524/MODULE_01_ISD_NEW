"""
bank_account.py
---------------
This module defines the BankAccount class for Assignment 1.

The BankAccount class demonstrates encapsulation via private attributes,
validation in the constructor, and controlled state changes through
public methods (update_balance, deposit, withdraw). String formatting
follows the assignment’s currency requirements.
"""
from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """
    Represents a bank account within the banking system.

    Attributes (private):
        __account_number (int): Unique account number.
        __client_number (int): Client number of the account holder.
        __balance (float): Current account balance.
    """

    def __init__(self, account_number: int, client_number: int, balance, date_created: date):
        """
        Initialize a new BankAccount with validation.

        Args:
            account_number (int): Account number (must be an integer).
            client_number (int): Client number (must be an integer).
            balance (any): Initial balance. If not convertible to float, defaults to 0.0.

        Raises:
            ValueError: If account_number is not an integer.
            ValueError: If client_number is not an integer.
        """
        # Validate account_number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate/assign balance (convertible to float → use float; otherwise 0.0)
        try:
            self.__balance = float(balance)
        except (TypeError, ValueError):
            self.__balance = 0.0

        # Validate / assign date_created
        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()


    # ---------------------------------------------------------------------
    # Accessors (properties)
    # ---------------------------------------------------------------------

    @property
    def account_number(self) -> int:
        """Return the private account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Return the private client number."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Return the current account balance."""
        return self.__balance
    
    @property
    def date_created(self) -> date:
        """Return the date when the account was created."""
        return self._date_created



    # ---------------------------------------------------------------------
    # Behavior
    # ---------------------------------------------------------------------

    def update_balance(self, amount) -> None:
        """
        Add 'amount' to the current balance if amount is convertible to float.

        Notes:
            - If amount cannot be converted to float, the balance is not changed.
            - Negative values are allowed (may reduce the balance).
        """
        try:
            delta = float(amount)
        except (TypeError, ValueError):
            # Invalid amount → no update
            return
        self.__balance += delta

    def deposit(self, amount) -> None:
        """
        Deposit a positive, numeric amount into the account.

        Validation:
            - If amount is not numeric/convertible → raise ValueError:
                "Deposit amount: {amount} must be numeric."
            - If amount <= 0 → raise ValueError with currency formatting:
                "Deposit amount: ${amount:,.2f} must be positive."

        On success, calls update_balance(amount).
        """
        # numeric?
        try:
            num = float(amount)
        except (TypeError, ValueError):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        # positive?
        if num <= 0:
            raise ValueError(f"Deposit amount: ${num:,.2f} must be positive.")

        # apply
        self.update_balance(num)

    def withdraw(self, amount) -> None:
        """
        Withdraw a positive, numeric amount that does not exceed current balance.

        Validation:
            - If amount is not numeric/convertible → raise ValueError:
                "Withdraw amount: {amount} must be numeric."
            - If amount <= 0 → raise ValueError with currency formatting:
                "Withdraw amount: ${amount:,.2f} must be positive."
            - If amount > balance → raise ValueError with currency formatting:
                "Withdraw amount: ${amount:,.2f} must not exceed the account balance: ${balance:,.2f}."

        On success, calls update_balance(-amount).
        """
        # numeric?
        try:
            num = float(amount)
        except (TypeError, ValueError):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

        # positive?
        if num <= 0:
            raise ValueError(f"Withdraw amount: ${num:,.2f} must be positive.")

        # not exceed balance
        if num > self.__balance:
            raise ValueError(
                f"Withdraw amount: ${num:,.2f} must not exceed the account balance: ${self.__balance:,.2f}."
            )

        # apply (note: update_balance always adds, so pass negative)
        self.update_balance(-num)

  
    def __str__(self) -> str:
        """
        Return the string representation of the account per spec.

        Format (with trailing newline):
            "Account Number: {account_number} Balance: ${balance:,.2f}\n"
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """Return the calculated service charges. Implemented by subclasses."""
        pass

