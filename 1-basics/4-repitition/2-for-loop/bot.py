MAX_FACES = 10
count = 0

print("How many ascii robots should I draw?")
user_number = int(input())

print("ok here I go!")

if (user_number < MAX_FACES):
  for count in range(0,user_number, 1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

else:
  print("Sorry you cannot exceed 10")
  for count in range(0, MAX_FACES, 1):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")

print("Done!")
