import math

numbers = [1,2,\ 
3,4]

def add_all_numbers_from_collection(
    number_one, number_two, number_three,
    number_four):
    return number_one+number_two + number_three +number_four

print (add_all_numbers_from_collection( *numbers ))