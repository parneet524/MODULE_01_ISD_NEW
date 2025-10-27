# patterns/strategy/minimum_balance_strategy.py
"""
Defines the MinimumBalanceStrategy class used for calculating service charges
for SavingsAccount instances.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Concrete strategy for calculating service charges based on whether
    a savings account meets its minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM = 1.00  # replaces old constant from SavingsAccount

    def __init__(self, minimum_balance: float):
        """Initialize with the account’s minimum balance requirement."""
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account) -> float:
        """
        Calculate service charges for SavingsAccount:
        - If balance >= minimum_balance → base charge (0.50)
        - Else → premium charge (1.00)
        """
        if account.balance >= self._minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.SERVICE_CHARGE_PREMIUM

        return round(service_charge, 2)
