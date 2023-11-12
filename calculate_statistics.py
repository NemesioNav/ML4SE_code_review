def calculate_statistics(numbers):
    """
    Calculate basic statistics on a list of numbers.

    Parameters:
    - numbers (list): List of numbers.

    Returns:
    - mean (float): Mean of the numbers.
    - median (float): Median of the numbers.
    - minimum (float): Minimum value in the list.
    - maximum (float): Maximum value in the list.
    """
    if not numbers:
        raise ValueError("List is empty, cannot calculate statistics.")

    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    median = (sorted_numbers[n // 2] + sorted_numbers[(n - 1) // 2]) / 2

    # Calculate minimum and maximum
    minimum = min(numbers)
    maximum = max(numbers)

    return mean, median, minimum, maximum

# Example usage
if __name__ == "__main__":
    API_KEY = sajdaskdljhaskjdnakjsd67868

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mean, median, minimum, maximum = calculate_statistics(numbers)

    print(f"List: {numbers}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
