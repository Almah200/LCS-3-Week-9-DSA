#!/usr/bin/python3
# A python program that reads the name of a month from the user as a string
# and that displays the number of days in that month


month = str(input("Enter a month: "))
list_of_months_31 = ["January", "March", "May", "July", "August", "October", "December"]
list_of_months_30 = ["April", "June", "September", "November"]
list_of_months_28 = ["February"]

if month in list_of_months_28:
    result = f"The month of {month} has 28 days"
elif month in list_of_months_30:
    result = f"The month of {month} has 30 days"
elif month in list_of_months_31:
    result = f"The month of {month} has 31 days"
else:
    result = "Input incorrect"
print(result)
