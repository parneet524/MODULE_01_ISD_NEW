"""
bank_account package initialization.
This allows importing all account classes using:
    from bank_account import *
"""

from .bank_account import BankAccount
from .chequing_account import ChequingAccount
from .savings_account import SavingsAccount
from .investment_account import InvestmentAccount

__all__ = [
    "BankAccount",
    "ChequingAccount",
    "SavingsAccount",
    "InvestmentAccount",
]
