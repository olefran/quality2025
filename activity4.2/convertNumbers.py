#!/usr/bin/env python3
"""
The program shall convert the numbers to binary and hexadecimal base.

The results shall be print on a screen and on
a file named ConvertionResults.txt
"""
import sys
import time


def main():
    """Compute binary and hex values from a file."""
    items = []
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <file_path>")
        sys.exit(1)

    try:
        # Open and read the file
        with open(sys.argv[1], 'r', encoding='UTF-8') as file:
            start_time = time.time()

            for line in file:
                for word in line.replace(',', ' ').split():
                    try:
                        num = float(word)
                        items.append(num)

                    except ValueError:
                        print(f'Error, "{word}" is not a valid number')

            print('Binary:')
            binary_list = [bin(int(x))[2:] for x in items]
            print(*binary_list)
            print('Hexadecimal:')
            hex_list = [hex(int(x))[2:] for x in items]
            print(*hex_list)
            exec_time = round((time.time() - start_time), 6)
            try:
                with open("ConvertionResults.txt", "w", encoding='UTF-8') as file:
                    file.write('Binary:\n')
                    for binary in binary_list:
                        file.write(binary + '\n')
                    file.write('Hexadecimal:\n')
                    for hexa in hex_list:
                        file.write(hexa + '\n')
                    file.write('Execution time: ' + str(exec_time) + ' seconds')
            except IOError as error_found:
                print(f"An error occurred: {error_found}")

            print(f"Execution time: {(time.time() - start_time):.6f} seconds")

    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")


if __name__ == "__main__":
    main()
