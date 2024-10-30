import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(100000, 999999)
        self.transactions = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)
        print(f"Deposited {amount} New balance: {self.balance}")

    def withdraw(self, amount, bank):
        if bank.bankrupt:
            print("The bank is bankrupt.Withdrawal does not allowed.")
        elif amount > self.balance:
            print("Withdrawal amount exceeded.")
        else:
            self.balance -= amount
            self.transactions.append(amount)
            print(f"Withdrawal {amount} New balance: {self.balance}")
            bank.update_total_balance()
    
    def transfer(self, amount, receiver_account, bank):
        if receiver_account is None:
                print("Account does not exist.")
        elif bank.bankrupt:
            print("The bank is bankrupt.Transfers does not allowed.")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            receiver_account.balance += amount
            self.transactions.append(amount)
            receiver_account.transactions.append(amount)
            print(f"Transfered {amount} New balance: {self.balance}")
            bank.update_total_balance()

    def loan_request(self, amount):
        if self.loan_count >= 2:
            print("Loan limit exceeded.")
        else:
            self.balance += amount
            self.loan_count += 1
            self.transactions.append(amount)
