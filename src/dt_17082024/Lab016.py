# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
import math

# Logic Building Formula

# Step 1 Figure out the inputs and output
# input -> r -> data type -> float
# pi -> 3.14 , math.pi
# power -> pow or ** -> any

# o/p -> float - area , print area

# Step 2
# rough logic =  area = 3.14 * pow(r,2)

# Step 3 - Write the logic

radius = float(input("enter radius of circle\n"))
print(radius)
area = math.pi * math.pow(radius, 2)
print("Area of circle is", area)
print(f"Area of circle is {area:.2f}")

# * --> mul
# ** --> Power


