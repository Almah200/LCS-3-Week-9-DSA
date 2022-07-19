#!/usr/bin/python3 

m = int(input("Enter a number: "))
if (m % 2) == 0:
    print("{} is Weird".format(m))
    
for m in range(2, 5):
    if (m % 2) != 0:
        print("{} is Not Weird".format(m))

for m in range(6, 20):
    if (m % 2) != 0:
        print("{} is Not Weird".format(m))
