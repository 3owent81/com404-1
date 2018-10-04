import math

print("Please enter a shape: cylinder or cone")
shape = input()

print("Please enter the radius of the shape")
radius = float(input())

print("Please enter the height of the shape")
height = float(input())

if (shape == "cylinder"):
  volume = math.pi * (radius ** 2) * height
  print("The volume of your", shape, "is", round(volume, 2))
elif (shape == "cone"):
  volume = (math.pi * (radius ** 2) * height) / 3
  print("The volume of your", shape, "is", round(volume, 2))

else:
  print("unknown shape")
