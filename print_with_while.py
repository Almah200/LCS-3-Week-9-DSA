def print_consonants_with_while_loop(given_string):
    vowels = ['a', 'e', 'e', 'o', 'u', 'y']
    i = 0
    # saving the consonants in this temporary list
    temp_list = list()
    while i < len(given_string):
        if given_string[i] not in vowels:
            temp_list.append(given_string[i])
        i += 1

    # now print all consonant but without adding ',' after the last one
    # reason why we saved them into the temp_list so we can know exactly the last one is a consonant
    j = 0
    while j < len(temp_list):
        # if j is at the last element, we print without ','
        if j == len(temp_list) - 1:
            print(temp_list[j], end='')
        else:
            print(temp_list[j], end=', ')
        j += 1
