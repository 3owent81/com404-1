# Ask user where to look and read user's response.
# Choices are as follows:
# 1) in the bedroom
# 2) in the bathroom
# 3) in the lab

print("Please enter one of the following locations")
print("[1] in the bedroom")
print("[2] in the bathroom")
print("[3] in the lab")
print("[4] somewhere else")

# Global variable because it is not in a block
place = input()

# In the bedroom:
#   Ask the user where in the bedroom
#   Choices are as follows:
#   1) under the bed  
#       found some socks but no battery
#   2) somewhere else
#       found some mess but no battery

if (place == "in the bedroom"):
  print("Where in the bedroom?")
  print("[1] under the bed")
  print("[2] somewhere else")
  
  # Local Variable because it is in a block
  bedroom_place = input()

  if (bedroom_place == "under the bed"):
    print("found some socks but no battery!")
  else:
    print("found some mess but no battery!")

# In the bathroom:
#   Ask the user where in the bathroom
#   Choices are as follows:
#   1) in the bathtub
#       found a rubber duck but no battery
#   2) somewhere else
#       it's wet but no battery

elif (place == "in the bathroom"):
  print("Where in the bathroom?")
  print("[1] in the bathtub")
  print("[2] somewhere else")
  
  bathroom_place = input()

  if (bathroom_place == "in the bathtub"):
    print("found a rubber duck but no battery!")
  else:
    print("its wet but no battery!")

# In the lab:
#   Ask the user where in the lab
#   Choices are as follows:
#   1) on the table  
#       found the battery
#   2) somewhere else
#       found some tools but no battery

elif (place == "in the lab"):
  print("Where in the lab?")
  print("[1] on the table")
  print("[2] somewhere else")
  
  lab_place = input()

  if (lab_place == "on the table"):
    print("found the battery!")
  else:
    print("found some tools but no battery!")

else:
  print("Not sure where that is but I will keep looking")
