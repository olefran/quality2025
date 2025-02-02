#!/usr/bin/env python3
"""
 The program shall identify all
distinct words and the frequency of them
(how many times the word “X” appears in
the file). The results shall be print on a
screen and on a file named
WordCountResults.txt
"""
import sys
import time


def main():
    """Compute Word count from a file."""
    items = []
    iters = {}
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <file_path>")
        sys.exit(1)

    try:
        # Open and read the file
        with open(sys.argv[1], 'r', encoding='UTF-8') as file:
            start_time = time.time()

            for line in file:
                for word in line.replace(',', ' ').split():
                    try:
                        num = str(word)
                        items.append(num)
                        if iters.get(num):
                            iters[num] = iters[num] + 1
                        else:
                            iters[num] = 1
                    except ValueError:
                        print(f'Error, "{word}" is not a valid word')

            exec_time = round((time.time() - start_time), 6)
            print('Word : Frequency')
            for key, value in iters.items():
                print(f"{key}: {value}")
            try:
                with open("WordCountResults.txt", "w", encoding='UTF-8') as file:
                    for key, value in iters.items():
                        file.write(f"{key}: {value}\n")
                    file.write('Execution time: ' + str(exec_time) + ' seconds')
            except IOError as error_found:
                print(f"An error occurred: {error_found}")

            print(f"Execution time: {exec_time} seconds")

    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")


if __name__ == "__main__":
    main()
