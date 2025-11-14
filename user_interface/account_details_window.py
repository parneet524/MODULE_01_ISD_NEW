__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Parneet Kaur"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):

    balance_updated = Signal(BankAccount)

    """
    A class used to display account details and perform bank account transactions.
    """
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        # Validate account parameter
        if isinstance(account, BankAccount):
            # Make a copy of the account so we do not directly modify original
            self.account = copy.copy(account)

            # Display initial account info
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Connect buttons to event handlers
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)
        else:
            # If the account is invalid, close the dialog
            self.reject()
            return
        
    # ---------------------------------------------------------
    # on_apply_transaction
    # ---------------------------------------------------------
    def on_apply_transaction(self) -> None:
        """
        Handles both deposit and withdrawal actions.
        """

        # Read user input
        amount_text = self.transaction_amount_edit.text().strip()

        # First: ensure the amount is numeric
        try:
            amount = float(amount_text)
        except Exception:
            QMessageBox.information(self, "Invalid Data",
                                    "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        # Determine which button was clicked
        try:
            sender = self.sender()
            transaction_type = ""

            if sender is self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            elif sender is self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            # Update balance label after successful transaction
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Clear and refocus amount box
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as ex:
            # If transaction failed, show message
            QMessageBox.information(
                self,
                f"{transaction_type} Failed",
                f"{ex}"
            )

            # Clear and refocus input
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    # ---------------------------------------------------------
    # on_exit
    # ---------------------------------------------------------
    def on_exit(self) -> None:
        """Closes the dialog window."""
        self.close()


