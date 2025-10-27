import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class (8 test cases)."""

    # Test Case 1
   
    def test_init_valid_inputs(self):
        """Test Case 1: Attributes are set to input values (superclass + subclass)."""
        acc = ChequingAccount(1234567, 22, 1000.00, date(2025, 10, 27), -100.0, 0.05)
        self.assertEqual(acc.account_number, 1234567)
        self.assertEqual(acc.client_number, 22)
        self.assertEqual(acc.balance, 1000.00)
        self.assertEqual(acc._ChequingAccount__overdraft_limit, -100.0)
        self.assertEqual(acc._ChequingAccount__overdraft_rate, 0.05)

    # Test Case 2
  
    def test_init_invalid_overdraft_limit(self):
        """Test Case 2: overdraft limit has invalid type."""
        acc = ChequingAccount(1111111, 33, 500.00, date(2025, 10, 27), "invalid", 0.05)
        self.assertEqual(acc._ChequingAccount__overdraft_limit, -100.0)

    # Test Case 3
   
    def test_init_invalid_overdraft_rate(self):
        """Test Case 3: overdraft rate has invalid type."""
        acc = ChequingAccount(1111111, 33, 500.00, date(2025, 10, 27), -100.0, "invalid")
        self.assertEqual(acc._ChequingAccount__overdraft_rate, 0.05)

    # Test Case 4
   
    def test_init_invalid_date_created(self):
        """Test Case 4: date created has invalid type."""
        acc = ChequingAccount(1111111, 33, 500.00, "2025-10-27", -100.0, 0.05)
        self.assertEqual(acc.date_created, date.today())

    # Test Case 5

    def test_get_service_charges_balance_greater_than_limit(self):
        """Test Case 5: balance greater than overdraft limit."""
        acc = ChequingAccount(123, 1, 0.00, date(2025, 10, 27), -100.0, 0.05)
        expected = 0.50
        actual = acc.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    # Test Case 6
   
    def test_get_service_charges_balance_less_than_limit(self):
        """Test Case 6: balance less than overdraft limit."""
        acc = ChequingAccount(123, 1, -600.0, date(2025, 10, 27), -100.0, 0.05)
        expected = 0.50 + (-100 - -600) * 0.05  # = 25.5
        actual = acc.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    # Test Case 7
   
    def test_get_service_charges_balance_equal_to_limit(self):
        """Test Case 7: balance equal to overdraft limit."""
        acc = ChequingAccount(123, 1, -100.0, date(2025, 10, 27), -100.0, 0.05)
        expected = 0.50
        actual = acc.get_service_charges()
        self.assertEqual(expected, round(actual, 2))

    # Test Case 8
   
    def test_str_output_format(self):
        """Test Case 8: appropriate value returned based on attribute values."""
        acc = ChequingAccount(1234567, 22, 1000.00, date(2025, 10, 27), -100.0, 0.05)
        output = str(acc)

        self.assertIn("Account Number: 1234567", output)
        self.assertIn("Balance: $1,000.00", output)
        self.assertIn("Overdraft Limit: $-100.00", output)
        self.assertIn("Overdraft Rate: 5.00%", output)
        self.assertIn("Account Type: Chequing", output)


if __name__ == "__main__":
    unittest.main()
