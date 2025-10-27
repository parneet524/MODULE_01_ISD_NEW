"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Parneet kaur"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from datetime import date
from client.client import Client
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount





# 2. Create a Client object with data of your choice.
client1 = Client(1010, "Susan", "Clark", "susanclark@pixell.com")




# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
cheq_acc = ChequingAccount(1234567, client1.client_number, 100.00, date(2024, 1, 1), -100.00, 5.00)

# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
save_acc = SavingsAccount(9483914, client1.client_number, 200.00, date(2024, 1, 1), 50.00)




# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
cheq_acc.attach(client1)
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
save_acc.attach(client1)






# 5a. Create a second Client object with data of your choice.
client2 = Client(2020, "Michael", "Brown", "michaelbrown@pixell.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
save_acc2 = SavingsAccount(5555555, client2.client_number, 1000.00, date(2023, 6, 1), 100.00)

# Attach observer
save_acc2.attach(client2)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
print("\n--- Performing Transactions ---\n")

# Transactions for ChequingAccount
try:
    cheq_acc.withdraw(30)  # Normal withdrawal
except Exception as e:
    print(e)

try:
    cheq_acc.withdraw(80)  # Should trigger low balance warning
except Exception as e:
    print(e)

try:
    cheq_acc.deposit(15000)  # Should trigger large transaction alert
except Exception as e:
    print(e)

# Transactions for SavingsAccount (client1)
try:
    save_acc.withdraw(160)  # Should trigger low balance warning
except Exception as e:
    print(e)

try:
    save_acc.deposit(60)  # Normal deposit
except Exception as e:
    print(e)

try:
    save_acc.deposit(12000)  # Should trigger large transaction
except Exception as e:
    print(e)

# Transactions for SavingsAccount (client2)
try:
    save_acc2.withdraw(950)  # Should trigger low balance warning
except Exception as e:
    print(e)

try:
    save_acc2.deposit(500)  # Normal
except Exception as e:
    print(e)

try:
    save_acc2.deposit(20000)  # Should trigger large transaction
except Exception as e:
    print(e)


# Print Final Account Information
print("\n--- Final Account Details ---\n")
print(cheq_acc)
print(save_acc)
print(save_acc2)

print("\nCheck the file 'output/observer_emails.txt' for simulated email alerts.\n")

