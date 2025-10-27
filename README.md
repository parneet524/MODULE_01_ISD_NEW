# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Parneet kaur

## Assignment
Assignment 1: Classes, Encapsulation, and Unit Testing

## Encapsulation
## Encapsulation
Encapsulation in this project is achieved by using **private attributes**, **public accessors**, and **method-based validation** to protect and manage data securely.

In the **`BankAccount`** class:
- All key data (`__account_number`, `__client_number`, and `__balance`) are declared as **private attributes**, preventing direct external modification.
- Controlled access is provided through **@property methods**, ensuring read-only access from outside the class.
- The constructor (`__init__`) validates inputs to ensure proper data types — integers for account and client numbers, and numeric values for balance (defaulting to 0.0 if invalid).
- Business logic in methods like `deposit()` and `withdraw()` enforces correct operations:
  - Deposits must be positive numeric values.
  - Withdrawals cannot exceed the current balance and must also be positive.
  - All exceptions are raised with clear, descriptive messages.

This structure ensures that sensitive account information is hidden and only modified through approved methods, maintaining **data integrity and system reliability**.

In the **`Client`** class:
- Private attributes (`__client_number`, `__first_name`, `__last_name`, and `__email_address`) are used to protect client data.
- Input validation ensures client numbers are integers, names are not blank, and email addresses are in valid format.
- Access to data is controlled through property methods, demonstrating encapsulation and maintaining data accuracy.

## Polymorphism

Polymorphism was achieved through the use of inheritance and method overriding in the BankAccount subclasses.

The abstract class `BankAccount` defines the abstract method `get_service_charges()`, which enforces that all subclasses — `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount` — must provide their own unique implementation of this method. Each subclass overrides `get_service_charges()` with logic specific to its account type:

- **ChequingAccount** calculates overdraft fees when the balance falls below the overdraft limit.  
- **SavingsAccount** applies a premium service charge when the balance drops below the minimum balance.  
- **InvestmentAccount** adds a management fee to the base charge unless the account is more than ten years old.

## Strategy Pattern
The **Strategy Pattern** is used in this application to make the calculation  
of service charges flexible and scalable. Instead of implementing all  
charge logic inside each account subclass, dedicated **strategy classes**  
handle each algorithm independently.

Each account type uses its own strategy:
- **ChequingAccount** → `OverdraftStrategy` calculates service charges  
  based on overdraft limit and rate.  
- **SavingsAccount** → `MinimumBalanceStrategy` determines charges  
  based on whether the account meets its minimum balance.  
- **InvestmentAccount** → `ManagementFeeStrategy` applies or waives  
  management fees depending on the account’s creation date.

This design supports easy extension — new account types or service  
charge rules can be added without modifying existing code, following  
the **Open/Closed Principle (OCP)** and promoting **loose coupling**.

---

## Testing
Unit tests (`pytest`) were created for all account types to verify  
the correct behaviour of `get_service_charges()` and other key methods.  
All test files (`test_chequing_account.py`, `test_savings_account.py`,  
`test_investment_account.py`) pass successfully after implementing  
the Strategy Pattern.

## Observer Pattern

The Observer Pattern is used in this project so clients can be automatically informed when something important happens in their bank accounts.  
Each bank account (Chequing, Savings, or Investment) acts as a subject, and each client acts as an observer.  
When a client is attached to an account, they get a simulated email alert if a large transaction occurs or if their balance goes below the minimum limit.  
This setup makes the system more organized and allows updates to happen without changing the main account code.
