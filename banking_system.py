import random

class Account:
    def __init__(self, name, pin, balance=0):
        self.account_number = str(random.randint(10000000, 99999999))
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        print(f"Account Balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Deposited {amount} successfully. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"Withdrew {amount} successfully. New Balance: {self.balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return
        self.pin = new_pin
        print("PIN changed successfully.")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        for t in self.transactions:
            print(t)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, pin, initial_deposit=0):
        account = Account(name, pin, initial_deposit)
        self.accounts[account.account_number] = account
        print(f"Account created successfully! Account Number: {account.account_number}")
        return account.account_number

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account is None:
            print("Account not found.")
            return None
        if account.pin != pin:
            print("Incorrect PIN.")
            return None
        return account

    def delete_account(self, account_number, pin):
        account = self.authenticate(account_number, pin)
        if account:
            del self.accounts[account_number]
            print("Account deleted successfully.")


def main():
    bank = Bank()

    while True:
        print("\n===== Simple Banking System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Change PIN")
        print("6. Show Transactions")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            pin = input("Set a 4-digit PIN: ")
            initial = float(input("Enter initial deposit amount: "))
            bank.create_account(name, pin, initial)

        elif choice == '2':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = bank.authenticate(acc_no, pin)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = bank.authenticate(acc_no, pin)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = bank.authenticate(acc_no, pin)
            if account:
                account.check_balance()

        elif choice == '5':
            acc_no = input("Enter account number: ")
            old_pin = input("Enter current PIN: ")
            account = bank.authenticate(acc_no, old_pin)
            if account:
                new_pin = input("Enter new PIN: ")
                account.change_pin(old_pin, new_pin)

        elif choice == '6':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = bank.authenticate(acc_no, pin)
            if account:
                account.show_transactions()

        elif choice == '7':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            bank.delete_account(acc_no, pin)

        elif choice == '8':
            print("Thank you for using our banking system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
