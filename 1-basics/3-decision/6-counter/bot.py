# Read 3 numbers from user
print("Please enter first number")
first_number = int(input())

print("Please enter a second number")
second_number = int(input())

print("Please enter a third number")
third_number = int(input())

# Work out which numbers are even or odd
evens = 0
odds = 0

if (first_number % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

if (first_number % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

if (first_number % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

# Display the result
print("Total number of evens is", evens)
print("The total number of odds", odds)
