print("Enter a word for Beep to say")
user_word = input()
characters = len(user_word)
MAX_CHARACTER = 4
count = 0

if(characters > MAX_CHARACTER):
  print("Too many characters")

else:
  for count in range (0, characters, 1):
    print(user_word)
