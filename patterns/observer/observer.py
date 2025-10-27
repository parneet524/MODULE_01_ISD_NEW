"""
Module: observer
Defines the Observer superclass that provides the interface for all
concrete observer classes to receive updates from subjects.
"""


class Observer:
    """
    Defines the interface for all observers that wish to receive updates
    from a subject (e.g., a BankAccount).
    """

    def update(self, message: str) -> None:
        """
        Receive update notifications from the Subject.

        Args:
            message (str): The message or event information sent by the Subject.

        This method is intended to be overridden by concrete subclasses.
        """
        raise NotImplementedError("Subclasses must implement the update() method.")
