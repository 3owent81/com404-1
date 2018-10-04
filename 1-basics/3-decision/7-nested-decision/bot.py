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

place = input()

# In the bedroom:
#   Ask the user where in the bedroom
#   Choices are as follows:
#   1) under the bed  
#       found some socks but no battery
#   2) somwhere else
#       found some mess but no battery

if (place == "in the bedroom"):
  print("Where in the bedroom?")
  print("[1] under the bed")
  print("[2] somewhere else")
  
  bedroom_place = input()

  if (bedroom_place == "under the bed"):
    print("found some socks but no battery!")
  else:
    print("found some mess but no battery!")
