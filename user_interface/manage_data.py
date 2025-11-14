__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
from datetime import date


# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************


def load_data() -> tuple[dict, dict]:
    """
    Loads client and account information from the CSV files.
    Returns two dictionaries:
        client_listing: {client_number: Client}
        accounts: {account_number: BankAccount subclass}
    """

    client_listing = {}
    accounts = {}

    # -----------------------------------------------------
    # READ CLIENT DATA
    # -----------------------------------------------------
    try:
        with open(clients_csv_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    client_number = int(row["client_number"])
                    first = row["first_name"]
                    last = row["last_name"]
                    email = row["email_address"]

                    client_obj = Client(
                        client_number=client_number,
                        first_name=first,
                        last_name=last,
                        email_address=email
                    )

                    client_listing[client_number] = client_obj

                except Exception as ex:
                    logging.error(f"Unable to create client: {ex}")

    except FileNotFoundError as ex:
        logging.error(f"Unable to open clients file: {ex}")

    # Helper to convert CSV field to float or None
    def to_float_or_none(value: str):
        if value is None:
            return None
        text = value.strip()
        if text == "" or text.lower() == "null":
            return None
        return float(text)

    # -----------------------------------------------------
    # READ ACCOUNT DATA
    # -----------------------------------------------------
    try:
        with open(accounts_csv_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    account_number = int(row["account_number"])
                    client_number = int(row["client_number"])
                    balance = float(row["balance"])
                    date_created = date.fromisoformat(row["date_created"])
                    account_type = row["account_type"]

                    overdraft_limit = to_float_or_none(row["overdraft_limit"])
                    overdraft_rate = to_float_or_none(row["overdraft_rate"])
                    minimum_balance = to_float_or_none(row["minimum_balance"])
                    management_fee = to_float_or_none(row["management_fee"])

                    # Choose which subclass to construct
                    if account_type == "ChequingAccount":
                        account_obj = ChequingAccount(
                            account_number=account_number,
                            client_number=client_number,
                            balance=balance,
                            date_created=date_created,
                            overdraft_limit=overdraft_limit,
                            overdraft_rate=overdraft_rate
                        )
                    elif account_type == "SavingsAccount":
                        account_obj = SavingsAccount(
                            account_number=account_number,
                            client_number=client_number,
                            balance=balance,
                            date_created=date_created,
                            minimum_balance=minimum_balance
                        )
                    elif account_type == "InvestmentAccount":
                        account_obj = InvestmentAccount(
                            account_number=account_number,
                            client_number=client_number,
                            balance=balance,
                            date_created=date_created,
                            management_fee=management_fee
                        )
                    else:
                        raise ValueError("Not a valid account type.")

                    # Only add accounts that belong to a real client
                    if client_number in client_listing:
                        accounts[account_number] = account_obj
                    else:
                        logging.error(
                            f"Bank Account: {account_number} contains invalid Client Number: {client_number}"
                        )

                except Exception as ex:
                    logging.error(f"Unable to create bank account: {ex}")

    except FileNotFoundError as ex:
        logging.error(f"Unable to open accounts file: {ex}")

    # -----------------------------------------------------
    # RETURN STATEMENT
    # -----------------------------------------------------
    return client_listing, accounts

    


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")