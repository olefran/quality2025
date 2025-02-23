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


class Hotel:
    def print_info(self):
        print(f"----- Hotel: {self.name} ----")
        if not self.reservations:
            print("No reservations registered")
        else:
            for reservation in self.reservations:
                reservation.print_info()
        print(f"---- End of Hotel: {self.name} ----")

    def add_reservation(self, customer, num):
        reservation = Reservation(customer, num)
        self.reservations.append(reservation)

    def modify(self, name):
        self.name = name

    def __init__(self,name):
        self.name = name
        self.reservations = []

class Reservation:
    def __init__(self, customer, num):
        self.customer = customer
        self.num = num

    def print_info(self):
        print(f"Reservation: {self.customer.name} on {self.num}")


class Customer:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("---- Customer ----")
        print(f"Name: {self.name}")
        print("----------------")

    def modify(self, name):
        self.name = name



def main():
    """Compute Word count from a file."""
    hotels = []
    customers = []
    # Check if both correct file paths are provided
    if len(sys.argv) != 3:
        print("Usage: python reservation_sys.py <Commands_file_path>")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r', encoding='UTF-8') as file:
            for line in file:
                if not line or line.startswith('#'):
                    continue

                try:
                    cmd = line.split(',')
                except TypeError:
                    print

    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
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
