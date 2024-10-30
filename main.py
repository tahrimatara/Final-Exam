from users import User
from admin import Bank

bank = Bank()

while True:
        print("1.User")
        print("2.Admin")
        print("3.Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print("a.Create Account")
            print("b.Deposit balance")
            print("c.Withdraw balance")
            print("d.Transfer balance")
            print("e.Request for Loan")
            print("f.Main Menu")
    
            user_choice = input("Enter Your choice: ")


            if user_choice == 'a':
                name = input("Enter Your Name: ")
                email = input("Enter Your Email: ")
                address = input("Enter Your Address: ")
                account_type = input("Enter Your Account type (Savings/Current): ")
                bank.create_account(name, email, address, account_type)

            elif user_choice == 'b':
                account_number = int(input("Enter account number: "))
                user = User(name,email,address,account_type)
                if user.account_number == account_number:
                    deposit_amount = int(input("Enter deposit amount: "))
                    User.deposit(deposit_amount)
                    Bank.update_total_balance()
                else:
                    print("Account not found.")

            elif user_choice== 'c':
                account_number = int(input("Enter account number: "))
                if user.account_number == account_number:
                        amount = int(input("Enter withdrawal amount: "))
                        User.withdraw(amount, Bank)
                else:
                    print("Account not found.")

            elif user_choice == 'd':
                sender_account_number = int(input("Enter your account number: "))
                receiver_account_number = int(input("Enter receiver account number: "))
                transfer_amount = int(input("Enter transfer amount: "))
                User.transfer(transfer_amount,receiver_account_number,bank)
                

            elif user_choice== 'e':
                account_number = int(input("Enter account number: "))
                if user.account_number == account_number:
                        loan_amount = int(input("Enter loan amount: "))
                        User.loan_request(loan_amount)
                else:
                    print("Account not found.")

            elif user_choice == 'f':
                continue


        elif choice == 2:
            print("a.Show All Users")
            print("b.Show Total Balance")
            print("c.Show Total Loan")
            print("d.Turn On Loan")
            print("e.Turn Off Loan")
            print("f.Exit")

            
            admin_choice = input("Enter choice: ")
            
            if admin_choice == 'a':
                bank.show_users()
            elif admin_choice == 'b':
                bank.total_balance()
            elif admin_choice == 'c':
                bank.total_loan()
            elif admin_choice == 'd':
                bank.on_loan()
            elif admin_choice == 'e':
                bank.off_loan()
            elif admin_choice == 'f':
                continue

        elif choice == 3:
            break

        else:
            print("Invalid choice")