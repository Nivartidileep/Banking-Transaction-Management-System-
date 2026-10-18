# Banking Transaction Management System

## Project Overview

The Banking Transaction Management System is a Core Python project that
simulates basic banking operations. The system allows customers to
create bank accounts and perform operations such as deposits,
withdrawals, fund transfers, balance enquiry, transaction history, and
account closure. The project is designed to demonstrate Python
fundamentals, functions, Object-Oriented Programming, exception
handling, validation, and TXT file handling. ---

## Problem Statement

Banks manage multiple customers and account operations such as deposits,
withdrawals, fund transfers, and balance checks. The objective of this
project is to build a Python banking application that performs these
operations with proper validation and transaction logic. ---

## Objectives

-   Register customers.

-   Create bank accounts.

-   Deposit money.

-   Withdraw money.

-   Transfer money between accounts.

-   Check account balance.

-   Maintain minimum balance.

-   Display transaction history.

-   Close accounts after satisfying the required conditions.

-   Store account records using a TXT file.

-   ## Apply Core Python and OOP concepts in a practical project.

## Features

1.  Customer Registration The system accepts:

-   Customer ID
-   Customer name
-   Phone number
-   Account number It validates the customer and account information
    before creating an account.

2.  Account Creation A new account is created with an initial minimum
    balance of ₹500.
3.  Deposit Customers can deposit money into their accounts. The system
    does not allow:

-   Zero amount
-   Negative amount

4.  Withdrawal Customers can withdraw money from their accounts. The
    system checks:

-   Amount must be greater than zero.
-   Sufficient balance must be available.
-   Minimum balance of ₹500 must be maintained.

5.  Fund Transfer Money can be transferred from one account to another.
    The system validates:

-   Sender account
-   Receiver account
-   Transfer amount
-   Minimum balance
-   Same-account transfer

6.  Balance Enquiry Customers can check their current account balance.
7.  Transaction History The system stores and displays previous
    transactions such as:

-   Deposits
-   Withdrawals
-   Transfers
-   Received transfers
-   Account opening

8.  Account Closure An account can be closed only when its balance is
    zero.
9.  File Handling Account information and transaction history are stored
    in: bank_records.txt The records are loaded when the program starts
    and saved after account changes. ---

## Technologies Used

-   Python
-   Core Python
-   Object-Oriented Programming
-   JSON
-   TXT File Handling \## Python Modules Used

``` python
import json
import os
from datetime import datetime
---

Python Concepts Used
Variables
Used to store customer details, account numbers, amounts, and transaction information.
Operators
Arithmetic and comparison operators are used for banking calculations and validation.
Conditional Statements
if, elif, and else are used for decision-making.
Loops
A while loop is used to continuously display the banking menu until the user exits.
Strings
Strings are used for names, account numbers, transaction messages, and error messages.
Dictionaries
```

The banking system uses a dictionary to store account objects using
account numbers as keys. \### Functions / Methods

Different methods are used for different banking operations. \###
Classes and Objects

The project uses: - Customer - Account - BankingSystem \### Constructor

The **init**() method initializes object data. \### Inheritance

The Account class inherits from the Customer class.

``` python
class Account(Customer):
Encapsulation
```

The account balance is protected using a private attribute:

``` python
self.__balance
Exception Handling
try, except, and raise are used to handle invalid operations and user input.
```

### File Handling

## The json, open(), load(), and dump() functions are used to save and retrieve account records from the TXT file.

## Project Structure

Banking-Transaction-Management-System/

``` text
│
├── banking_system.py
├── bank_records.txt
└── README.md
```

## File Description

  File                Description
  ------------------- ----------------------------------------
  banking_system.py   Main Python application
  bank_records.txt    Stores account and transaction records
  README.md           Project documentation

## bank_records.txt contains runtime account data. Do not commit real customer or financial information to a public repository.

## How to Run the Project

### Step 1: Install Python

Install Python 3.x on your computer. \### Step 2: Clone the repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 3: Open the project folder

``` bash
cd Banking-Transaction-Management-System
```

### Step 4: Run the program

``` bash
python banking_system.py
---

Main Menu
```

The application displays: ===== BANKING MANAGEMENT SYSTEM =====

1.  Customer Registration / Account Creation

2.  Deposit

3.  Withdrawal

4.  Fund Transfer

5.  Balance Enquiry

6.  Transaction History

7.  Account Closure

8.  ## Exit

## Sample Workflow

Step 1 -- Create Account Enter customer ID: C101 Enter customer name:
Dileep Enter phone number: 9876543210 Create account number: 1001

Customer registered and account created. Step 2 -- Deposit Enter account
number: 1001 Enter deposit amount: Rs.1000

Deposit successful. Step 3 -- Balance Enquiry Account holder: Dileep
Available balance: Rs.1500.00 Step 4 -- Withdrawal Enter account number:
1001 Enter withdrawal amount: Rs.200

Withdrawal successful. Step 5 -- Fund Transfer Create another account
and transfer money between the two accounts. The system updates both
account balances and records the transaction history. ---

## Validation and Exception Handling

The project handles invalid situations such as: - Invalid account
number - Duplicate account number - Duplicate customer ID - Invalid
phone number - Zero transaction amount - Negative transaction amount -
Insufficient balance - Minimum balance violation - Transfer to the same
account - Invalid menu choice - Invalid numeric input - Missing or
invalid saved records Example:

``` python
try:
    amount = float(input("Enter amount: "))
```

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

except ValueError as error: print("Error:", error) ---

## Test Cases

  -----------------------------------------------------------------------
  Test Case               Input / Situation       Expected Result
  ----------------------- ----------------------- -----------------------
  TC01                    Valid customer          Account created
                          registration            

  TC02                    Duplicate account       Registration rejected
                          number                  

  TC03                    Deposit ₹1,000          Balance increases

  TC04                    Deposit negative amount Transaction rejected

  TC05                    Withdraw valid amount   Balance decreases

  TC06                    Withdraw excessive      Transaction rejected
                          amount                  

  TC07                    Withdraw causing        Transaction rejected
                          minimum balance         
                          violation               

  TC08                    Valid fund transfer     Both balances updated

  TC09                    Transfer to same        Transaction rejected
                          account                 

  TC10                    Balance enquiry         Current balance
                                                  displayed

  TC11                    Transaction history     Previous transactions
                                                  displayed

  TC12                    Close account with      Closure rejected
                          non-zero balance        

  TC13                    Close account with zero Account closed
                          balance                 

  TC14                    Restart application     Saved records loaded
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## OOP Design

### Customer Class

Stores basic customer information.

``` text
Customer
 ├── customer_id
 ├── name
 └── phone
```

### Account Class

Inherits customer information and manages account operations.

``` text
Customer
    ↑
Account
```

The Account class contains: - Account number - Private balance -
Transaction history - Deposit method - Withdrawal method - Transfer
method - Balance method \### BankingSystem Class

Controls the complete banking workflow. It manages: - Account
collection - Customer registration - File storage - Deposits -
Withdrawals - Transfers - Balance enquiry - Transaction history -
Account closure - Menu ---

## GitHub Commit Strategy

Use meaningful commits instead of uploading everything with one commit.
Example:

``` bash
git init

git add README.md
git commit -m "Add project documentation"

git add banking_system.py
git commit -m "Add banking management system"

git add .
git commit -m "Add validation and transaction features"
```

Then push the project:

``` bash
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
---

Suggested GitHub Repository Name
Banking-Transaction-Management-System
---
```

## Future Enhancements

The project can be improved by adding: - User login and authentication -
Password protection - MySQL database - Admin dashboard - Account types
such as Savings and Current - Interest calculation - ATM functionality -
PDF bank statements - Better audit logging - Secure password hashing -
Web interface using Flask or Django ---

## Learning Outcomes

Through this project, I learned how to: - Apply Core Python concepts to
a practical problem. - Design classes and objects. - Use constructors
and inheritance. - Apply encapsulation. - Create reusable functions and
methods. - Handle exceptions. - Validate user input. - Process banking
transactions. - Maintain transaction history. - Store persistent data
using file handling. - Organize a Python project for GitHub. ---

## Project Demonstration

During the project demonstration, the following workflow can be shown:
\### Customer Registration

``` text
        ↓
```

### Account Creation

``` text
        ↓
Deposit
        ↓
Balance Enquiry
        ↓
Withdrawal
        ↓
Create Second Account
        ↓
Fund Transfer
        ↓
Transaction History
        ↓
```

### Account Closure

``` text
        ↓
Exit
---

Conclusion
```

The Banking Transaction Management System demonstrates how Core Python
can be used to build a practical application. The project combines
Python fundamentals, functions, Object-Oriented Programming, validation,
exception handling, collections, and file handling to implement a simple
banking workflow. This project helped me understand transaction
processing, class design, data validation, and practical Python
application development.
"# Banking-Transaction-Management-System" 
