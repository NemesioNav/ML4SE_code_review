import math

def circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    area = (math.pi * radius) ** 2
    return area

def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a*2 + b*2)
    return hypotenuse

def print_greeting(name):
    print("Hello, " + name + "! Welcome to the Python error script.")

# Calculate the area of a circle
radius = 5
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")

# Attempt to calculate hypotenuse with negative values
side_a, side_b = 3, -4
hypotenuse = calculate_hypotenuse(side_a, side_b)
print(f"The hypotenuse of a right-angled triangle with sides {side_a} and {side_b} is: {hypotenuse}")

# Print a greeting with an undefined variable
print_greeting(username)

# Access an index that is out of range in a list
colors = ["red", "green", "blue"]
print("The fourth color in the list is: " + colors[3])
