MAX_FACES = 10
count = 0

print("How many ascii robots should I draw?")
user_number = int(input())

print("ok here I go!")

if (user_number < MAX_FACES):
  while (count < user_number):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    count = count + 1

else:
  print("Sorry you cannot exceed 10")
  while (count < MAX_FACES):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    count = count + 1

print("Done!")
