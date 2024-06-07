class Finance:
    def investment(self):
        principal_amount = float(input("Enter the principal amount: "))
        interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
        investment_time = int(input("Enter the number of years the money is invested: "))

        future_value = ((principal_amount * interest_rate * investment_time) / 100) + principal_amount

        print(f"The future value of the investment is: {future_value}")

    def loan_approval(self):
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: "))
        loan_amount = float(input("Enter the loan amount you are requesting: "))

        if self.check_credit_score(credit_score) and self.check_loan_amount(loan_amount, income):
            print("Loan Approved")
        else:
            print("Loan Denied")

    def check_credit_score(self, credit_score):
        return credit_score >= 700

    def check_loan_amount(self, loan_amount, income):
        return loan_amount <= (income * 0.3)

# Example usage:
finance = Finance()
choice = int(input("Enter the choice (1 for Investment, 2 for Loan): "))

if choice == 1:
    finance.investment()
elif choice == 2:
    finance.loan_approval()
else:
    print("Invalid choice")
