# Declare useful constants
DAYS_IN_YEAR = 365.25

# Read in age of user
print("Please enter your age (years)")
age_in_years = int(input())

# Calculate age in days
age_in_days = age_in_years * DAYS_IN_YEAR

# Display result
print("Your age in days is", age_in_days)
