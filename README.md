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
