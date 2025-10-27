# bank_account/investment_account.py
"""
Defines the InvestmentAccount class which uses the ManagementFeeStrategy
to calculate service charges.
"""

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy


class InvestmentAccount(BankAccount):
    """Represents an investment account using the Strategy Pattern."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initialize InvestmentAccount using BankAccount attributes + subclass attributes.

        :param management_fee: The management fee applied to the account.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # validate management fee
        try:
            self.__management_fee = float(management_fee)
        except (TypeError, ValueError):
            self.__management_fee = 2.55

        # assign ManagementFeeStrategy
        self.__strategy = ManagementFeeStrategy(date_created, self.__management_fee)

    def get_service_charges(self) -> float:
        """
        Calculate and return service charges using the ManagementFeeStrategy.
        """
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Return formatted string showing account details per spec."""
        base_info = super().__str__()

        # determine if fee should be waived (10 years old or older)
        ten_years_ago = date.today().replace(year=date.today().year - 10)
        if self.date_created <= ten_years_ago:
            fee_display = "Waived"
        else:
            fee_display = f"${self.__management_fee:,.2f}"

        return (
            f"{base_info}\n"
            f"Date Created: {self.date_created} "
            f"Management Fee: {fee_display} "
            f"Account Type: Investment"
        )

