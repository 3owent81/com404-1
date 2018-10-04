# The modulo operator (%) returns the remainder after division. 
# For example,
# 4 % 2 returns 0.
# 5 % 3 returns 2.
# if a number is even, it will have a remainder of 0 after dividing it by 2.

print("Enter a whole number")
user_number = int(input())

if (user_number % 2 == 0):
  print("The number", user_number,"is even")
else:
  print("the number is odd")
