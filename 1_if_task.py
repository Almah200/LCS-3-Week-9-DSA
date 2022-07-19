#!/usr/bin/python3 
# Given an integer, m, perform the following conditional actions
# Print "Weird" if even number
# Print "Not Weird" if odd number in range(2, 5)
# Print "Weird" if m is odd number in range(6, 20)
# Print "Not Weird" if odd and greater than 20

m = int(input("Enter a number: "))
if (m % 2) == 0:
    print("{} is Weird".format(m))
else:
    if 2 <= m < 5:
        print("{} is Not Weird".format(m))

    elif 6 <= m < 20 or 2 <= m < 5 or m > 20:
        print("{} is Not Weird".format(m))
