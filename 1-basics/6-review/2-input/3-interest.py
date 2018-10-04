# Read in current amount from user
print("Please enter the current amount (£)")
current_amount = float(input())

print("Please enter interest rate (%)")
interest_rate = float(input())

interest_amount = (interest_rate / 100) * current_amount
new_amount = current_amount + interest_amount

# Display the result
print("Your new amount is £" + str( round(new_amount, 2) ) )
