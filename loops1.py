Maximum_number = int(input('Please enter an integer: '))
for number in range(1, Maximum_number + 1):
    if(number % 2 != 0):
        print('{}'.format(number))