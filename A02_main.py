"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Parneet Kaur"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from datetime import date
from bank_account import ChequingAccount, SavingsAccount, InvestmentAccount


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    cheq = ChequingAccount(1234567, 22, -600.00, date.today(), -100.00, 0.05)
except Exception as e:
    print(e)


# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    save = SavingsAccount(9483914, 44, 1000.00, date.today(), 50.00)
except Exception as e:
    print(e)

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    cheq.deposit(700.00)
    print(cheq)
    print("Service Charges:", cheq.get_service_charges())
except Exception as e:
    print(e)

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    save = SavingsAccount(9483914, 44, 1000.00, date.today(), 50.00)
except Exception as e:
    print(e)


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(save)
    print("Service Charges:", save.get_service_charges())
except Exception as e:
    print(e)


# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    save.withdraw(960.00)
    print(save)
    print("Service Charges:", save.get_service_charges())
except Exception as e:
    print(e)


print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    invest_recent = InvestmentAccount(2341234, 33, 19329.21, date(2024, 1, 1), 1.99)
except Exception as e:
    print(e)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(invest_recent)
    print("Service Charges:", invest_recent.get_service_charges())
except Exception as e:
    print(e)


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    invest_old = InvestmentAccount(1948371, 55, 11329.65, date(2013, 1, 1), 2.00)
except Exception as e:
    print(e)


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    print(invest_old)
    print("Service Charges:", invest_old.get_service_charges())
except Exception as e:
    print(e)


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    cheq.withdraw(cheq.get_service_charges())
    save.withdraw(save.get_service_charges())
    invest_recent.withdraw(invest_recent.get_service_charges())
    invest_old.withdraw(invest_old.get_service_charges())
except Exception as e:
    print(e)



# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
try:
    print(cheq)
    print(save)
    print(invest_recent)
    print(invest_old)
except Exception as e:
    print(e)