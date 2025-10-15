"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client


class TestClient(unittest.TestCase):
    """
    Test suite for the Client class, aligned with the Excel test plan.
    """

    # --- Test Case 1: __init__ — Attributes set to input values. ---
    def test_init_happy_path_sets_attributes(self):
        """Object created successfully; all attributes set to correct values."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")

        # Property checks
        self.assertEqual(1010, obj.client_number)
        self.assertEqual("Susan", obj.first_name)
        self.assertEqual("Clark", obj.last_name)
        self.assertEqual("susan@example.com", obj.email_address)

        # Name-mangled private checks
        self.assertEqual(1010, obj._Client__client_number)
        self.assertEqual("Susan", obj._Client__first_name)
        self.assertEqual("Clark", obj._Client__last_name)
        self.assertEqual("susan@example.com", obj._Client__email_address)

    # --- Test Case 2: __init__ — Exception when invalid client number. ---
    def test_init_raises_when_client_number_not_integer(self):
        """ValueError raised when client_number is not an int."""
        with self.assertRaises(ValueError):
            Client("ABC", "Susan", "Clark", "susan@example.com")

    # --- Test Case 3: __init__ — Exception when blank first_name. ---
    def test_init_raises_when_first_name_blank(self):
        """ValueError raised when first_name is blank after stripping."""
        with self.assertRaises(ValueError):
            Client(1011, " ", "Clark", "susan@example.com")

    # --- Test Case 4: __init__ — Exception when blank last_name. ---
    def test_init_raises_when_last_name_blank(self):
        """ValueError raised when last_name is blank after stripping."""
        with self.assertRaises(ValueError):
            Client(1012, "Susan", " ", "susan@example.com")

    # --- Test Case 5: __init__ — Invalid email defaults to Pixell address. ---
    def test_invalid_email_defaults_to_pixell_river_address(self):
        """Invalid email sets email_address to 'email@pixell-river.com'."""
        obj = Client(2020, "John", "Smith", "invalidemail")
        self.assertEqual("email@pixell-river.com", obj.email_address)
        self.assertEqual("email@pixell-river.com", obj._Client__email_address)

    # --- Test Case 6–9: Accessors return expected values. ---
    def test_client_number_property_returns_value(self):
        """client_number property returns integer client number (e.g., 1010)."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")
        self.assertEqual(1010, obj.client_number)

    def test_first_name_property_returns_value(self):
        """first_name property returns 'Susan' (from happy path)."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")
        self.assertEqual("Susan", obj.first_name)

    def test_last_name_property_returns_value(self):
        """last_name property returns 'Clark' (from happy path)."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")
        self.assertEqual("Clark", obj.last_name)

    def test_email_address_property_returns_value(self):
        """email_address property returns 'susan@example.com' (from happy path)."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")
        self.assertEqual("susan@example.com", obj.email_address)

    # --- Test Case 10: __str__ — Returns string in expected format. ---
    def test_str_returns_expected_format_with_newline(self):
        """__str__ returns 'Clark, Susan [1010] - susan@example.com' followed by newline."""
        obj = Client(1010, "Susan", "Clark", "susan@example.com")
        expected = "Clark, Susan [1010] - susan@example.com\n"
        self.assertEqual(expected, str(obj))


if __name__ == "__main__":
    unittest.main()