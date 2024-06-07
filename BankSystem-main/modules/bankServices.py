import random
import time

class ATM:
    def __init__(self):
        self.balance_in_acc = 100000.0

    def green_pin(self):
        answer = int(input("Do you want to generate a green pin for:\n1. Credit Card\n2. Debit Card\n"))
        card_no = int(input("Enter your card number:\n"))
        cif_no = int(input("Enter your CIF number:\n"))

        max_num = 1000000
        green_pin = random.randint(0, max_num)
        
        print(f"The GREEN PIN number is: {green_pin}")

    def change_pin(self):
        card_no = int(input("Enter your card number:\n"))
        cif_no = int(input("Enter your CIF number:\n"))

        otp = random.randint(15, 1000000)
        print(f"The OTP number is: {otp}")

        entered_otp = int(input("Re-enter the OTP here to verify:\n"))

        if entered_otp == otp:
            print("OTP verified!\n")
            new_pass = int(input("Enter new password:\n"))
            confirm_pass = int(input("Confirm new password:\n"))

            if new_pass == confirm_pass:
                print("NEW PASSWORD SET SUCCESSFULLY!")
            else:
                print("Re-enter confirmation password:")
                confirm_pass = int(input())
                print("NEW PASSWORD SET SUCCESSFULLY!\n")
        else:
            print("Invalid OTP")

    def balance_inquiry(self):
        print(f"\nThe balance in your bank account is {self.balance_in_acc}\n")

    def deposit_in_acc(self):
        amount = float(input("Enter the amount you want to deposit in your account:\n"))

        if amount < 0:
            print("The amount is invalid!\n")
            return

        self.balance_in_acc += amount
        print(f"\nThe amount {amount} has been successfully deposited!")
        print(f"The total amount now in your account is {self.balance_in_acc}\n")

    def withdraw(self):
        amount = float(input("Enter the amount you want to withdraw:\n"))

        if amount > self.balance_in_acc or amount < 0:
            print("The amount you entered is exceeding the balance (Insufficient amount)\n")
            return

        self.balance_in_acc -= amount
        print(f"{amount} successfully withdrawn from your account")
        print(f"The total amount now in your account is {self.balance_in_acc}\n")

def main():
    atm = ATM()

    while True:
        print("\n----------TEAM 8 ATM-----------")
        print("---------WELCOMES YOU----------")
        print("Choose your option:")
        print("1. Generate Green Pin")
        print("2. Change CARD password")
        print("3. Account Details (withdraw, deposit, check balance)")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.green_pin()
        elif choice == 2:
            atm.change_pin()
        elif choice == 3:
            while True:
                print("1. Check Balance")
                print("2. Deposit Amount")
                print("3. Withdraw Amount")
                print("4. Exit")
                
                options = int(input("Enter your choice: "))

                if options == 1:
                    atm.balance_inquiry()
                elif options == 2:
                    atm.deposit_in_acc()
                elif options == 3:
                    atm.withdraw()
                elif options == 4:
                    print("Thank You! Visit Again!")
                    break
                else:
                    print("Invalid! Please choose between the given numbers!")
        elif choice == 4:
            print("Thank You! Visit Again!")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
