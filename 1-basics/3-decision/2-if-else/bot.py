# Read in directions from user
print(" Please enter a direction from the following:")
print("...w to move up")
print("...a to move left")
print("...s to move down")
print("...d to move right")

direction = input()

if (direction == "w"):
  print("I am moving up!")
else:
  print("I am not sure what direction that is")
