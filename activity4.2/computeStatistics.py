#!/usr/bin/env python3
"""
The program shall compute.

Descriptive statistics from a file containing
numbers. The results shall be print on a
screen and on a file named
StatisticsResults.txt
"""
import sys
import time


def variance(sq_diffs, count):
    """Compute Variance."""
    return sum(sq_diffs) / count


def median_calc(count, items):
    """Compute Median."""
    if count % 2:
        median = items[(count+1)//2]
    else:
        median = (items[count//2] + items[count//2+1]) / 2
    return median


def main():
    """Compute descriptive statistics from a file."""
    count = 0
    total = 0
    items = []
    iters = {}
    max_iter = 1
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <file_path>")
        sys.exit(1)

    try:
        # Open and read the file
        with open(sys.argv[1], 'r', encoding='UTF-8') as file:
            start_time = time.time()

            for line in file:
                for word in line.replace(',', ' ').split():
                    try:
                        num = float(word)
                        count = count + 1
                        total = total + num
                        items.append(num)
                        if iters.get(num):
                            iters[num] = iters[num] + 1
                            if iters[num] > max_iter:
                                max_iter = iters[num]
                        else:
                            iters[num] = 1
                    except ValueError:
                        print(f'Error, "{word}" is not a valid number')

            mean = total / count
            mode = [x for x, value in iters.items() if value == max_iter]
            items.sort()
            median = median_calc(count, items)
            print(f'Mean: {mean}\nMode: {" ".join(map(str, mode))}')
            print(f'Median: {median}')

            sq_diffs = [(x - mean) ** 2 for x in items]
            exec_time = round((time.time() - start_time), 6)
            print(f'Variance: {variance(sq_diffs, count)}\n')
            print(f'Standart Deviation: {variance(sq_diffs,count) **.5}\n')
            try:
                with open("StatisticsResults.txt", "w", encoding='UTF-8') as file:
                    file.write('Mean: ' + str(mean) + '\n')
                    file.write('Mode: ' + " ".join(map(str, mode)) + '\n')
                    file.write('Median: ' + str(median) + '\n')
                    file.write('Variance: ' + str(variance) + '\n')
                    file.write('Standart Deviation' + str(variance(sq_diffs,count) ** .5) + '\n')
                    file.write('Execution time: ' + str(exec_time) + ' seconds')
            except IOError as error_found:
                print(f"An error occurred: {error_found}")

            print(f"Execution time: {exec_time} seconds")

    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")


if __name__ == "__main__":
    main()
