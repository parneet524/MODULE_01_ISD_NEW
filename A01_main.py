""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.

This script tests the functionality of both classes by performing valid and invalid
operations such as creating clients, depositing, withdrawing, and triggering exceptions
to confirm validation logic.

"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Parneet kaur"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    print("=== Step 1: Creating a valid Client ===")
    client = None
    try:
        client = Client(1010, "Susan", "Clark", "susan@example.com")
    except ValueError as e:
        print(e)

    # 2. Declare a BankAccount object with an initial value of None.
    print("\n=== Step 2: Declaring BankAccount variable ===")
    bank_account = None


    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    print("\n=== Step 3: Creating a valid BankAccount ===")
    try:
        if client is not None:
            bank_account = BankAccount(20019, client.client_number, 250.00)
    except ValueError as e:
        print(e)


    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    print("\n=== Step 4: Creating BankAccount with invalid balance ===")
    try:
        invalid_account = BankAccount(20020, client.client_number, "invalid")
        print(invalid_account)
    except ValueError as e:
        print(e)


    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print("\n=== Step 5: Printing valid Client and BankAccount ===")
    if client is not None:
        print(client)
    if bank_account is not None:
        print(bank_account)



    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
    print("=== Step 6: Deposit non-numeric value ===")
    if bank_account is not None:
        try:
            bank_account.deposit("abc")
        except ValueError as e:
            print(e)


    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
    print("=== Step 7: Deposit negative value ===")
    if bank_account is not None:
        try:
            bank_account.deposit(-100)
        except ValueError as e:
            print(e)


    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    print("=== Step 8: Withdraw valid amount ===")
    if bank_account is not None:
        try:
            bank_account.withdraw(50.00)
            print(bank_account)
        except ValueError as e:
            print(e)


    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    print("=== Step 9: Withdraw non-numeric value ===")
    if bank_account is not None:
        try:
            bank_account.withdraw("xyz")
        except ValueError as e:
            print(e)


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    print("=== Step 10: Withdraw negative value ===")
    if bank_account is not None:
        try:
            bank_account.withdraw(-10)
        except ValueError as e:
            print(e)


    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    print("=== Step 11: Withdraw exceeding balance ===")
    if bank_account is not None:
        try:
            bank_account.withdraw(9999)
        except ValueError as e:
            print(e)
 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print("\n=== Step 12: Final BankAccount state ===")
    if bank_account is not None:
        print(bank_account)


if __name__ == "__main__":
    main()