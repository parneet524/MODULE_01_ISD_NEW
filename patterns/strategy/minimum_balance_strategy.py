"""
Module: minimum_balance_strategy
Defines the MinimumBalanceStrategy class used for calculating service charges
for SavingsAccount instances.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Concrete strategy class for calculating service charges based on the account's
    minimum balance. Used by SavingsAccount instances.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initialize the minimum balance strategy.

        :param minimum_balance: The required minimum balance for the account.
        """
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account) -> float:
        """
        Calculates the service charge for a SavingsAccount.

        Logic (based on original SavingsAccount.get_service_charges):
        - If the account balance is below the required minimum balance:
            Apply the base service charge + service charge premium.
        - Otherwise:
            Apply only the base service charge.

        :param account: BankAccount object (SavingsAccount) to calculate charges for.
        :return: Calculated service charge (float)
        """
        balance = account.get_balance()

        if balance < self._minimum_balance:
            # Balance below minimum → apply premium
            service_charge = self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        else:
            # Normal service charge
            service_charge = self.BASE_SERVICE_CHARGE

        return round(service_charge, 2)