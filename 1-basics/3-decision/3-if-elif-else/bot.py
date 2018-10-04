# Read in directions from user
print(" Please enter a direction from the following:")
print("...w to move up")
print("...a to move left")
print("...s to move down")
print("...d to move right")

direction = input()

if (direction == "w"):
  print("I am moving up!")
elif (direction == "a"):
  print("I am moving left!")
elif (direction == "s"):
  print("I am moving down!")
elif (direction == "d"):
  print("I am moving right!")
else:
  print("I am not sure what direction that is")
