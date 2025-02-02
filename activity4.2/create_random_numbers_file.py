#!/usr/bin/env python3
import random

def create_random_numbers_file(filename, min_numbers=10, max_numbers=100, min_value=0, max_value=1000):
    """
    Creates a file with a random number of random numbers.

    Parameters:
    filename (str): The name of the file to create.
    min_numbers (int): The minimum number of random numbers to generate.
    max_numbers (int): The maximum number of random numbers to generate.
    min_value (int): The minimum value for the random numbers.
    max_value (int): The maximum value for the random numbers.
    """
    # Generate a random number of numbers
    num_numbers = random.randint(min_numbers, max_numbers)

    # Generate the random numbers
    random_numbers = [random.randint(min_value, max_value) for _ in range(num_numbers)]

    # Write the numbers to the file
    with open(filename, 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")

    print(f"Created file '{filename}' with {num_numbers} random numbers.")

if __name__ == "__main__":
    # Customize the file name and ranges
    filename = "random_numbers.txt"
    min_numbers = 10  # Minimum number of random numbers
    max_numbers = 500  # Maximum number of random numbers
    min_value = -67858     # Minimum value for random numbers
    max_value = 68877   # Maximum value for random numbers

    # Create the file
    create_random_numbers_file(filename, min_numbers, max_numbers, min_value, max_value)
