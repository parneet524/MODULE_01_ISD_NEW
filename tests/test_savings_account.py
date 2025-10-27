"""
test_savings_account.py
-----------------------
Unit tests for the SavingsAccount class.
Tests constructor validation, service charge logic, and string output formatting.
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    """Unit tests for SavingsAccount class."""

    def test_init_valid_inputs(self):
        """Test that all attributes are set correctly with valid inputs."""
        acc = SavingsAccount(9483914, 22, 1000.00, date(2025, 10, 27), 50.00)
        self.assertEqual(acc.account_number, 9483914)
        self.assertEqual(acc.client_number, 22)
        self.assertEqual(acc.balance, 1000.00)
        # Name mangling to access private attribute
        self.assertEqual(acc._SavingsAccount__minimum_balance, 50.00)

    def test_init_invalid_minimum_balance(self):
        """Test that invalid minimum_balance defaults to 50.00."""
        acc = SavingsAccount(9483914, 22, 1000.00, date(2025, 10, 27), "invalid")
        self.assertEqual(acc._SavingsAccount__minimum_balance, 50.00)

    def test_get_service_charges_balance_greater_than_minimum(self):
        """Balance > minimum_balance should return BASE_SERVICE_CHARGE (0.50)."""
        acc = SavingsAccount(9483914, 22, 500.00, date(2025, 10, 27), 100.00)
        expected = 0.50
        actual = round(acc.get_service_charges(), 2)
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_equal_to_minimum(self):
        """Balance = minimum_balance should return BASE_SERVICE_CHARGE (0.50)."""
        acc = SavingsAccount(9483914, 22, 50.00, date(2025, 10, 27), 50.00)
        expected = 0.50
        actual = round(acc.get_service_charges(), 2)
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_less_than_minimum(self):
        """Balance < minimum_balance should return BASE_SERVICE_CHARGE * PREMIUM (1.00)."""
        acc = SavingsAccount(9483914, 22, 40.00, date(2025, 10, 27), 50.00)
        expected = 1.00
        actual = round(acc.get_service_charges(), 2)
        self.assertEqual(expected, actual)

    def test_str_output(self):
        """Ensure __str__ returns the correct formatted string."""
        acc = SavingsAccount(9483914, 22, 1000.00, date(2025, 10, 27), 50.00)
        result = str(acc)
        self.assertIn("Account Number: 9483914", result)
        self.assertIn("Balance: $1,000.00", result)
        self.assertIn("Minimum Balance: $50.00", result)
        self.assertIn("Account Type: Savings", result)


if __name__ == "__main__":
    unittest.main()
