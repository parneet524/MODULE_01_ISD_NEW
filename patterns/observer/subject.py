"""
Module: subject
Defines the Subject superclass for managing observers that are notified of state changes.
"""

from patterns.observer.observer import Observer


class Subject:
    """
    The Subject class maintains a list of observers and notifies them of any changes.
    """

    def __init__(self) -> None:
        """Initialize an empty list of observers."""
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject if it isn't already attached.

        Args:
            observer (Observer): The observer to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Detach (remove) an observer from the subject.

        Args:
            observer (Observer): The observer to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Notify all attached observers of a change or event.

        Args:
            message (str): The message to send to all observers.
        """
        for observer in self._observers:
            observer.update(message)
