#  This script will calculate the user’s monthly savings based on inputted monthly income and expenses
#  It will then project these savings over a year, assuming a fixed interest rate

#user input for financial details
monthly_income = int(input("Enter your monthly income : "))
monthly_expenses = int(input("Enter your total monthly expenses :"))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

# Project Annual Saving
interest_rate = 0.05
projected_savings =  monthly_savings  * 12 + (monthly_savings * 12 * 0.05)

#print the  user’s monthly savings, the projected annual savings after including interest.
print(f"your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is : {projected_savings}")


