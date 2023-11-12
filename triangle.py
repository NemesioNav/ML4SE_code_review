def calculate_triangle_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

# Example Usage:
if __name__ == "__main__":
    # Enter the lengths of the sides of the triangle
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    # Calculate and display the perimeter
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print("The perimeter of the triangle is:", perimeter)
