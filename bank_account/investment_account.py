"""
investment_account.py
---------------------
Defines the InvestmentAccount class, a subclass of BankAccount.
Implements management fee handling and specific service charge logic.
"""

from datetime import date, timedelta
from bank_account.bank_account import BankAccount


class InvestmentAccount(BankAccount):
    """
    Represents an Investment Account intended for long-term savings.
    """

    # Constant representing the cutoff date for 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created, management_fee: float):
        """
        Initialize an InvestmentAccount.

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date or any): Date account was created.
            management_fee (float): Management fee applied to the account.

        Validation:
            - If management_fee cannot convert to float → defaults to 2.55.
            - If date_created is not instance of date → defaults to today's date.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # management_fee validation
        try:
            self.__management_fee = float(management_fee)
        except (TypeError, ValueError):
            self.__management_fee = 2.55

    # ----------------------------------------------------------------------
    # Behavior
    # ----------------------------------------------------------------------

    def get_service_charges(self) -> float:
        """
        Return the calculated service charges.

        Rules:
            - If date_created <= TEN_YEARS_AGO → service charge = BASE_SERVICE_CHARGE
            - Else → service charge = BASE_SERVICE_CHARGE + management_fee
        """
        if self.date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self) -> str:
        """
        Return formatted InvestmentAccount details.

        Examples:
            Account Number: 2341234 Balance: $19,329.21
            Date Created: 2024-01-01 Management Fee: $1.99 Account Type: Investment

            Account Number: 1948371 Balance: $11,329.65
            Date Created: 2013-01-01 Management Fee: Waived Account Type: Investment
        """
        base_str = super().__str__()
        # Determine if older than 10 years
        if self.date_created <= self.TEN_YEARS_AGO:
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        return (
            f"{base_str}\n"
            f"Date Created: {self.date_created} "
            f"Management Fee: {fee_display} "
            f"Account Type: Investment"
        )
