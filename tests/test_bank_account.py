"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """
    Unit tests for the BankAccount class.

    Each test method aligns with one row in the unit test plan
    for Assignment 1. Together, they verify initialization, 
    encapsulation, and transaction correctness.
    """

    # ---------------------------------------------------------
    # Constructor (__init__) Tests
    # ---------------------------------------------------------

    def test_init_sets_attributes(self):
        """
        Test 1: Ensure attributes are set correctly when valid inputs are provided.
        """
        acc = BankAccount(20019, 1010, 100.00)
        self.assertEqual(20019, acc.account_number)
        self.assertEqual(1010, acc.client_number)
        self.assertEqual(100.00, round(acc.balance, 2))

        # Private attributes check via name mangling
        self.assertEqual(20019, acc._BankAccount__account_number)
        self.assertEqual(1010, acc._BankAccount__client_number)
        self.assertEqual(100.00, round(acc._BankAccount__balance, 2))

    def test_init_non_numeric_balance_defaults_zero(self):
        """
        Test 2: If balance is non-numeric, it should default to 0.00.
        """
        acc = BankAccount(20019, 1010, "abc")
        self.assertEqual(0.00, round(acc.balance, 2))

    def test_init_raises_when_account_number_not_int(self):
        """
        Test 3: Ensure ValueError is raised if account number is not an integer.
        """
        with self.assertRaisesRegex(ValueError, "Account number must be an integer"):
            BankAccount("X", 1010, 0.0)

    def test_init_raises_when_client_number_not_int(self):
        """
        Test 4: Ensure ValueError is raised if client number is not an integer.
        """
        with self.assertRaisesRegex(ValueError, "Client number must be an integer"):
            BankAccount(20019, "X", 0.0)

    # ---------------------------------------------------------
    # Accessor Tests (Getters)
    # ---------------------------------------------------------

    def test_account_number_getter(self):
        """
        Test 5: account_number property should return correct value.
        """
        acc = BankAccount(20019, 1010, 100.0)
        self.assertEqual(20019, acc.account_number)

    def test_client_number_getter(self):
        """
        Test 6: client_number property should return correct value.
        """
        acc = BankAccount(20019, 1010, 100.0)
        self.assertEqual(1010, acc.client_number)

    def test_balance_getter(self):
        """
        Test 7: balance property should return correct value.
        """
        acc = BankAccount(20019, 1010, 100.0)
        self.assertEqual(100.00, round(acc.balance, 2))

    # ---------------------------------------------------------
    # update_balance Tests
    # ---------------------------------------------------------

    def test_update_balance_positive_amount(self):
        """
        Test 8: Balance should increase correctly when a positive amount is added.
        """
        acc = BankAccount(20019, 1010, 100.00)
        acc.update_balance(25.50)
        self.assertEqual(125.50, round(acc.balance, 2))

    def test_update_balance_negative_amount(self):
        """
        Test 9: Balance should decrease correctly when a negative amount is applied.
        """
        acc = BankAccount(20019, 1010, 100.00)
        acc.update_balance(-40)
        self.assertEqual(60.00, round(acc.balance, 2))

    def test_update_balance_non_numeric_ignored(self):
        """
        Test 10: Balance should remain unchanged when a non-numeric amount is given.
        """
        acc = BankAccount(20019, 1010, 50.00)
        acc.update_balance("abc")
        self.assertEqual(50.00, round(acc.balance, 2))

    # ---------------------------------------------------------
    # deposit Tests
    # ---------------------------------------------------------

    def test_deposit_valid_amount(self):
        """
        Test 11: Ensure deposit correctly increases the balance for valid input.
        """
        acc = BankAccount(20019, 1010, 100.00)
        acc.deposit(75.34)
        self.assertEqual(175.34, round(acc.balance, 2))

    def test_deposit_non_positive_raises(self):
        """
        Test 12: Ensure ValueError is raised when deposit is zero or negative.
        """
        acc = BankAccount(20019, 1010, 100.00)
        with self.assertRaisesRegex(ValueError, r"Deposit amount: \$0\.00 must be positive\."):
            acc.deposit(0)

    # ---------------------------------------------------------
    # withdraw Tests
    # ---------------------------------------------------------

    def test_withdraw_valid_amount(self):
        """
        Test 13: Ensure withdraw correctly decreases balance when valid.
        """
        acc = BankAccount(20019, 1010, 200.00)
        acc.withdraw(75.34)
        self.assertEqual(124.66, round(acc.balance, 2))

    def test_withdraw_non_positive_raises(self):
        """
        Test 14: Ensure ValueError is raised when withdraw amount is non-positive.
        """
        acc = BankAccount(20019, 1010, 100.00)
        with self.assertRaisesRegex(ValueError, r"Withdraw amount: \$0\.00 must be positive\."):
            acc.withdraw(0)

    def test_withdraw_exceeds_balance_raises(self):
        """
        Test 15: Ensure ValueError is raised when withdraw exceeds current balance.
        """
        acc = BankAccount(20019, 1010, 50.00)
        with self.assertRaisesRegex(
            ValueError,
            r"Withdraw amount: \$75\.00 must not exceed the account balance: \$50\.00\."
        ):
            acc.withdraw(75)

    # ---------------------------------------------------------
    # __str__ Tests
    # ---------------------------------------------------------

    def test_str_format(self):
        """
        Test 16: Ensure string representation matches the expected formatted output.
        """
        acc = BankAccount(20019, 1010, 6764.67)
        expected = "Account Number: 20019 Balance: $6,764.67\n"
        self.assertEqual(expected, str(acc))


if __name__ == "__main__":
    unittest.main()