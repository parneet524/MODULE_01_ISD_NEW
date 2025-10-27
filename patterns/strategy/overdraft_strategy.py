# patterns/strategy/overdraft_strategy.py
"""
Module: overdraft_strategy
Defines the OverdraftStrategy class which handles service charge calculations
for accounts with overdraft capability.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Concrete strategy class for calculating service charges based on overdraft usage.
    Used by ChequingAccount instances.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initialize the overdraft strategy with limit and rate.

        :param overdraft_limit: Maximum overdraft limit for the account.
        :param overdraft_rate: Rate applied to overdraft service charge.
        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account) -> float:
        """
        Calculates service charges for a ChequingAccount based on overdraft usage.

        Logic (same as original get_service_charges from ChequingAccount):
        - If balance >= overdraft_limit → base service charge only.
        - If balance < overdraft_limit → apply overdraft fee.
        """
        balance = account.balance

        if balance >= self._overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            # Calculate extra charge for overdraft difference
            service_charge = self.BASE_SERVICE_CHARGE + (self._overdraft_limit - balance) * self._overdraft_rate

        return round(service_charge, 2)
