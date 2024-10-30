from users import User

class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance_amount = 0
        self.total_loan_amount = 0
        self.loan_status  = True
        self.bankrupt = False

    def create_account(self, name, email, address, account_type):
        account = User(name, email, address, account_type)
        self.accounts.append(account)

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)    
            else:
                 print("Account not found.")
        
    def show_users(self):
        print("List of Users\n")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")

    def total_balance(self):
        print(f"Total balance: {self.total_balance_amount}")

    def total_loan(self):
        print(f"Total loan: {self.total_loan_amount}")

    def off_loan(self):
        self.loan_status = False
        print("Loan status off successfully.")

    def on_loan(self):
        self.loan_status = True
        print("Loan status on successfully.")

    def check_bankrupt(self):
        if self.total_balance <= 0:
            self.bankrupt = True
        else:
            self.bankrupt = False

    def update_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        self.total_balance = total
        self.check_bankrupt()
