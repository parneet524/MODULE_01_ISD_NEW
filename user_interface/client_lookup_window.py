__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()

        # Load both dictionaries from load_data()
        self.client_listing, self.accounts = load_data()

        # Connect GUI buttons and events
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)

    def on_lookup_client(self):
        """
        Handles looking up the client and displaying their accounts.
        """

        # Get input from text box
        client_number_text = self.client_number_edit.text().strip()

        # Convert to int
        try:
            client_number = int(client_number_text)
        except Exception:
            QMessageBox.information(self, "Input Error",
                                    "The client number must be a numeric value.")
            self.reset_display()
            return

        # Check if client exists
        if client_number not in self.client_listing:
            QMessageBox.information(
                self,
                "Not Found",
                f"Client number: {client_number} not found."
            )
            self.reset_display()
            return

        # Get the Client object
        client = self.client_listing[client_number]

        # Display client name label
        full_name = f"{client.first_name} {client.last_name}"
        self.client_info_label.setText(f"Client Name: {full_name}")

        # Clear any old rows
        self.account_table.setRowCount(0)

        # Fill the account table
        for account in self.accounts.values():
            if account.client_number == client_number:

                row = self.account_table.rowCount()
                self.account_table.insertRow(row)

                # Create items
                item_num = QTableWidgetItem(str(account.account_number))
                item_bal = QTableWidgetItem(f"${account.balance:,.2f}")
                item_date = QTableWidgetItem(str(account.date_created))
                item_type = QTableWidgetItem(account.__class__.__name__)

                # Add to table
                self.account_table.setItem(row, 0, item_num)
                self.account_table.setItem(row, 1, item_bal)
                self.account_table.setItem(row, 2, item_date)
                self.account_table.setItem(row, 3, item_type)

        # Adjust columns so they fit the data
        self.account_table.resizeColumnsToContents()

    def on_text_changed(self):
        """
        Clears table rows whenever the text field changes.
        """
        self.account_table.setRowCount(0)

    def on_select_account(self, row: int, column: int):
        """
        Opens the Account Details window when a row is clicked.
        """

        # Account number is stored in column 0
        item = self.account_table.item(row, 0)

        # No item?
        if item is None or item.text().strip() == "":
            QMessageBox.information(self, "Invalid Selection",
                                    "Please select a valid record.")
            return

        # Try converting
        try:
            account_number = int(item.text())
        except Exception:
            QMessageBox.information(self, "Invalid Selection",
                                    "Please select a valid record.")
            return

        # Check if account exists
        if account_number not in self.accounts:
            QMessageBox.information(self, "No Bank Account",
                                    "Bank Account selected does not exist.")
            return

        # Valid → open details window
        account = self.accounts[account_number]
        dlg = AccountDetailsWindow(account)
        dlg.exec()

        
