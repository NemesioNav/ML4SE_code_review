def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [5, 7, 9, 2, 4, 6]

result = calculate_average(numbers)
print("The average is: " result)