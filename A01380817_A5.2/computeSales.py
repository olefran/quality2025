#!/usr/bin/env python3
"""
The program shall determine price sales of a json catalog

The program:
Will recieve a Json catalog as first argument
with valid 'title' and 'price' tags.
Will recieve a Json catalog as a second argument
with valid 'Quantity' and 'Product' tags.
Will write results on file 'SaleResults.txt
on relative execution path.
"""
import sys
import time
import json


def main():
    """Compute Word count from a file."""
    price_table = {}
    total = 0
    price = {}
    sales = {}
    # Check if both correct file paths are provided
    if len(sys.argv) != 3:
        print("Usage: python computeSales <Price_file_path> <Sales_file_path>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r', encoding='UTF-8') as price_file:
            price = json.load(price_file)
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
        sys.exit(1)

    try:
        with open(sys.argv[2], 'r', encoding='UTF-8') as sales_file:
            sales = json.load(sales_file)
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[2]}' was not found.")
        sys.exit(1)

    start_time = time.time()
    for _, key in enumerate(price):
        try:
            price_table[key['title']] = key['price']
        except KeyError:
            print(f"'price' tag not found for {key['title']}")

    for _, key in enumerate(sales):
        total = total + price_table[key['Product']]*key['Quantity']

    exec_time = round((time.time() - start_time), 6)
    print('TOTAL:')
    print(f'{total:.2f}')
    print(f"Execution time: {exec_time:.6f} seconds")
    try:
        with open("SalesResults.txt", "w", encoding='UTF-8') as file:
            file.write(f"Total:\n{total}\n")
            file.write(f"Execution time: {exec_time:.6f} seconds")
    except IOError as error_found:
        print(f"An error occurred: {error_found}")


if __name__ == "__main__":
    main()
