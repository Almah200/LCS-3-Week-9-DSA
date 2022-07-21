# Dictionary
def roman_to_int(roman_string):
    # check if roman_string argument is a string, otherwise return 0 as described by the exercise
    if type(roman_string) != str or roman_string is None:
        return 0
    # save the roman numerals in a dictionary with key-value pair where key is the
    # roman number and value is the corresponding numeral number
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # create list to save corresponding value of roman each roman string
    numeral_values = list()

    # if only one character in the string, simply return the corresponding value
    if len(roman_string) == 1:
        return roman_numerals[roman_string]

    # if roman string is more than one character we should consider some cases explained inside
    if len(roman_string) > 1:

        # By default, we do the sum of the characters to get the numeral value.
        # Example: II = 2 because 1+1 = 2. So in our list numeral_values will be : [1, 1].
        # But IV = 4, not 5. Because we don’t do 1+5 but 5-1
        # Same for XC = 90, not 110. Because we don’t do 10+100 but 100-10
        # Same for CD = 90, not 110. Because we don’t do 10+100 but 100-10
        # looping through each character of the string
        for i in range(0, len(roman_string)):
            try:
                # if we have "I" then the next character is "V" or "X", like IX or IV,
                # it means we should do
                if roman_string[i] == "I" and \
                        (roman_string[i + 1] == "V" or
                         roman_string[i + 1] == "X") \
                        or roman_string[i] == "X" and \
                        (roman_string[i + 1] == "C" or
                         roman_string[i + 1] == "L") \
                        or roman_string[i] == "C" and \
                        (roman_string[i + 1] == "D" or
                         roman_string[i + 1] == "M"):
                    numeral_values.append(-int(roman_numerals[roman_string[i]]))
                else:
                    numeral_values.append(int(roman_numerals[roman_string[i]]))
            except IndexError:
                numeral_values.append(int(roman_numerals[roman_string[i]]))
                pass
    return sum(numeral_values)


#  List question 1
def get_sum_in_list(my_list=[], num=0):
    for i in range(len(my_list)):
        ptr = my_list[i]
        sub_list = my_list[i + 1:]
        for j in range(len(sub_list)):
            if ptr + sub_list[j] == num:
                return tuple((i, i + 1 + j))


#  List question 2
def get_index_of_number_in_list(my_list=[], num=0):
    for i in range(len(my_list)):
        if my_list[i] == num:
            return i


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_index_of_number_in_list([1, 3, 5, 6], 6))
