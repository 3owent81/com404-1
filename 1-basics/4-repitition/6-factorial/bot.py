print("Enter a number")
user_number = int(input())
factorial = 1
count = 0

for count in range(user_number, 0, -1):
  factorial = factorial * count

print("The factorial of your number is", factorial)
