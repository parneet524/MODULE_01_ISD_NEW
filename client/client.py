"""
client.py
---------
This module defines the Client class used in Assignment 1 for Intermediate Software Development.

The Client class represents an individual customer in the banking system.
It demonstrates encapsulation through private attributes and the use of
accessor (property) methods. It also includes validation for all attributes
to ensure data integrity.
"""

from email_validator import validate_email, EmailNotValidError


class Client:
    """
    Represents a client within the banking system.

    Attributes:
        __client_number (int): The unique client number (private).
        __first_name (str): The client's first name (private).
        __last_name (str): The client's last name (private).
        __email_address (str): The client's email address (private).
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initialize a new Client instance with validated and encapsulated data.

        Args:
            client_number (int): The unique client number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: If client_number is not an integer.
            ValueError: If first_name or last_name is blank after stripping whitespace.
        """
        # Validate client_number is integer
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate first_name (not blank)
        first_name = first_name.strip()
        if first_name == "":
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name

        # Validate last_name (not blank)
        last_name = last_name.strip()
        if last_name == "":
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name

        # Validate email_address using the email-validator library
        try:
            validate_email(email_address, check_deliverability=False)
            self.__email_address = email_address
        except EmailNotValidError:
            # Default email used if invalid
            self.__email_address = "email@pixell-river.com"

    # ---------------------------
    # Accessor Methods (Properties)
    # ---------------------------

    @property
    def client_number(self) -> int:
        """
        Accessor for the private client_number attribute.

        Returns:
            int: The client's unique number.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Accessor for the private first_name attribute.

        Returns:
            str: The client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Accessor for the private last_name attribute.

        Returns:
            str: The client's last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Accessor for the private email_address attribute.

        Returns:
            str: The client's validated email address.
        """
        return self.__email_address

   
    def __str__(self) -> str:
        """
        Returns a formatted string representation of the Client.

        Returns:
            str: The formatted client information in the following format:

            "{last_name}, {first_name} [{client_number}] - {email_address}\\n"

        Example:
            Clark, Susan [1010] - susanclark@pixell.com
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"

        