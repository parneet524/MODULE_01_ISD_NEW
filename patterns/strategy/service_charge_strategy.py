"""
Module: service_charge_strategy
Defines the abstract base class for all service charge calculation strategies.
"""

from abc import ABC, abstractmethod


class ServiceChargeStrategy(ABC):
    """
    Abstract base class representing a general strategy for calculating service charges.
    All concrete strategy classes (e.g., OverdraftStrategy, ManagementFeeStrategy, MinimumBalanceStrategy)
    will implement the calculate_service_charges method differently, depending on the account type.
    """

    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """
        Abstract method that must be implemented by all concrete strategy subclasses.
        Each subclass defines its own logic for calculating service charges based on the given account.

        :param account: BankAccount object to calculate service charges for
        :return: Calculated service charge (float)
        """
        pass
