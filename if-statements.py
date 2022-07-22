#!/usr/bin/python3
m = int(input())
if m % 2 == 0:
    print('Weird')
elif m % 2 != 0 and 2 >= m <=5:
    print('Not Weird')
elif m % 2 != 0 and 6 >= m <= 20:
    print('Weird')
elif m % 2 != 0 and m > 20:
    print('Not Weird'
