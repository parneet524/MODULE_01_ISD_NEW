import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount


class TestInvestmentAccount(unittest.TestCase):
    """Unit tests for the InvestmentAccount class."""

    def test_init_valid_inputs(self):
        """Attributes are set to parameter values."""
        acc = InvestmentAccount(1111, 22, 5000.00, date(2020, 1, 1), 2.00)
        self.assertEqual(acc.account_number, 1111)
        self.assertEqual(acc.client_number, 22)
        self.assertEqual(acc.balance, 5000.00)
        self.assertEqual(acc._InvestmentAccount__management_fee, 2.00)

    def test_init_invalid_management_fee(self):
        """Invalid management fee should default to 2.55."""
        acc = InvestmentAccount(1111, 22, 5000.00, date(2020, 1, 1), "invalid")
        self.assertEqual(acc._InvestmentAccount__management_fee, 2.55)

    def test_get_service_charges_more_than_10_years_old(self):
        """Date created more than 10 years ago should waive management fee."""
        acc = InvestmentAccount(2222, 33, 10000.00, date(2010, 1, 1), 2.00)
        expected = 0.50
        self.assertEqual(expected, round(acc.get_service_charges(), 2))

    def test_get_service_charges_exactly_10_years_old(self):
        """Date created exactly 10 years ago should waive management fee."""
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        acc = InvestmentAccount(3333, 44, 10000.00, ten_years_ago, 2.00)
        expected = 0.50
        self.assertEqual(expected, round(acc.get_service_charges(), 2))

    def test_get_service_charges_within_last_10_years(self):
        """Date created within last 10 years should include management fee."""
        acc = InvestmentAccount(4444, 55, 8000.00, date(2023, 1, 1), 2.00)
        expected = 0.50 + 2.00
        self.assertEqual(expected, round(acc.get_service_charges(), 2))

    def test_str_waived_fee(self):
        """__str__ should show 'Waived' for accounts older than 10 years."""
        acc = InvestmentAccount(5555, 66, 10000.00, date(2010, 1, 1), 2.00)
        result = str(acc)
        self.assertIn("Management Fee: Waived", result)
        self.assertIn("Account Type: Investment", result)

    def test_str_management_fee_displayed(self):
        """__str__ should show fee for accounts within last 10 years."""
        acc = InvestmentAccount(6666, 77, 10000.00, date(2023, 1, 1), 2.00)
        result = str(acc)
        self.assertIn("Management Fee: $2.00", result)
        self.assertIn("Account Type: Investment", result)


if __name__ == "__main__":
    unittest.main()
