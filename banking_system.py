
import json
import os
from datetime import datetime


FILE_NAME = "bank_records.txt"
MINIMUM_BALANCE = 500


class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone


class Account(Customer):
    def __init__(self, customer_id, name, phone,
                 account_number, balance=500):
        super().__init__(customer_id, name, phone)
        self.account_number = account_number
        self.__balance = balance
        self.transactions = []

    def get_balance(self):
        return self.__balance

    def add_transaction(self, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{time} - {message}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        self.__balance += amount
        self.add_transaction(f"Deposited Rs.{amount:.2f}")
        return "Deposit successful."

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if self.__balance - amount < MINIMUM_BALANCE:
            raise ValueError(
                "Insufficient funds or minimum balance violation."
            )

        self.__balance -= amount
        self.add_transaction(f"Withdrawn Rs.{amount:.2f}")
        return "Withdrawal successful."

    def transfer(self, receiver, amount):
        if receiver.account_number == self.account_number:
            raise ValueError("Cannot transfer to the same account.")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if self.__balance - amount < MINIMUM_BALANCE:
            raise ValueError("Insufficient balance for transfer.")

        # Update both accounts only after validation.
        self.__balance -= amount
        receiver.__balance += amount

        self.add_transaction(
            f"Transferred Rs.{amount:.2f} to "
            f"{receiver.account_number}"
        )
        receiver.add_transaction(
            f"Received Rs.{amount:.2f} from "
            f"{self.account_number}"
        )
        return "Fund transfer successful."

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "account_number": self.account_number,
            "balance": self.__balance,
            "transactions": self.transactions
        }


class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.load_records()

    def load_records(self):
        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r") as file:
                records = json.load(file)

            for record in records:
                account = Account(
                    record["customer_id"],
                    record["name"],
                    record["phone"],
                    record["account_number"],
                    record["balance"]
                )
                account.transactions = record.get("transactions", [])
                self.accounts[account.account_number] = account

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Could not load saved records.")

    def save_records(self):
        with open(FILE_NAME, "w") as file:
            json.dump(
                [a.to_dict() for a in self.accounts.values()],
                file,
                indent=4
            )

    def register_customer(self):
        customer_id = input("Enter customer ID: ").strip()
        name = input("Enter customer name: ").strip()
        phone = input("Enter phone number: ").strip()
        account_number = input("Create account number: ").strip()

        if not all([customer_id, name, phone, account_number]):
            print("All fields are required.")
            return

        if account_number in self.accounts:
            print("Account number already exists.")
            return

        if any(a.customer_id == customer_id
               for a in self.accounts.values()):
            print("Customer ID already exists.")
            return

        if not phone.isdigit() or len(phone) != 10:
            print("Enter a valid 10-digit phone number.")
            return

        account = Account(
            customer_id, name, phone, account_number
        )
        account.add_transaction("Account opened with Rs.500.00")
        self.accounts[account_number] = account
        self.save_records()
        print("Customer registered and account created.")

    def find_account(self):
        number = input("Enter account number: ").strip()
        account = self.accounts.get(number)

        if account is None:
            print("Account not found.")
        return account

    def deposit_money(self):
        account = self.find_account()
        if account is None:
            return

        try:
            amount = float(input("Enter deposit amount: Rs."))
            print(account.deposit(amount))
            self.save_records()
        except ValueError as error:
            print("Error:", error)

    def withdraw_money(self):
        account = self.find_account()
        if account is None:
            return

        try:
            amount = float(input("Enter withdrawal amount: Rs."))
            print(account.withdraw(amount))
            self.save_records()
        except ValueError as error:
            print("Error:", error)

    def transfer_money(self):
        print("Sender account:")
        sender = self.find_account()
        if sender is None:
            return

        print("Receiver account:")
        receiver = self.find_account()
        if receiver is None:
            return

        try:
            amount = float(input("Enter transfer amount: Rs."))
            print(sender.transfer(receiver, amount))
            self.save_records()
        except ValueError as error:
            print("Error:", error)

    def balance_enquiry(self):
        account = self.find_account()
        if account:
            print("Account holder:", account.name)
            print("Available balance: Rs.",
                  f"{account.get_balance():.2f}")

    def transaction_history(self):
        account = self.find_account()
        if account:
            print("\n--- Transaction History ---")
            if not account.transactions:
                print("No transactions available.")
            for transaction in account.transactions:
                print(transaction)

    def close_account(self):
        account = self.find_account()
        if account is None:
            return

        if account.get_balance() != 0:
            print("Withdraw or transfer the remaining balance first.")
            print("Account closure requires zero balance.")
            return

        del self.accounts[account.account_number]
        self.save_records()
        print("Account closed successfully.")

    def run(self):
        while True:
            print("\n===== BANKING MANAGEMENT SYSTEM =====")
            print("1. Customer Registration / Account Creation")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Fund Transfer")
            print("5. Balance Enquiry")
            print("6. Transaction History")
            print("7. Account Closure")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            try:
                if choice == "1":
                    self.register_customer()
                elif choice == "2":
                    self.deposit_money()
                elif choice == "3":
                    self.withdraw_money()
                elif choice == "4":
                    self.transfer_money()
                elif choice == "5":
                    self.balance_enquiry()
                elif choice == "6":
                    self.transaction_history()
                elif choice == "7":
                    self.close_account()
                elif choice == "8":
                    print("Thank you for using our banking system.")
                    break
                else:
                    print("Invalid choice. Select 1 to 8.")
            except OSError as error:
                print("File operation failed:", error)


if __name__ == "__main__":
    bank = BankingSystem()
    bank.run()
