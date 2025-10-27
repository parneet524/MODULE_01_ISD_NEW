"""
Module: management_fee_strategy
Defines the ManagementFeeStrategy class used for calculating service charges
for InvestmentAccount instances.
"""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Concrete strategy class for calculating service charges based on
    management fees and the age of an account. Used by InvestmentAccount instances.
    """

    # Constant: represents 10 years ago from today's date
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initialize the management fee strategy.

        :param date_created: The date when the investment account was created.
        :param management_fee: The management fee associated with the account.
        """
        self._date_created = date_created
        self._management_fee = management_fee
    
    def calculate_service_charges(self, account) -> float:
        """
        Calculates the service charge for an InvestmentAccount.

        Logic (based on original InvestmentAccount.get_service_charges):
        - If the account is 10 years old or older → only base service charge applies.
        - Otherwise → base service charge + management fee.
        """
        if self._date_created <= self.TEN_YEARS_AGO:
            # Account is at least 10 years old → no management fee, only base charge
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            # Newer than 10 years → base charge + management fee
            service_charge = self.BASE_SERVICE_CHARGE + self._management_fee

        return round(service_charge, 2)

