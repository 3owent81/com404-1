print("How many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

print("Enter characters")
character = str(input())

for count in range(0, rows, 1):
  for number in range(0,columns, 1):
    print(character, end="\t")
  print()
