import math

# You get to enter the values of the coordinates using these.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# It calculates the distance using the distance formula of two points,
d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

# This part gives the answer
print(f"The distance between the two points is: {d:.2f}")
