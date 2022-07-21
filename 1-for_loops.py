#!/usr/bin/python3
# Print a python program that takes an integer
# and print all odd numbers up to the integer

number = int(input("Enter a number: "))

for i in range(number):
    if i % 2 != 0:
        print(i)

