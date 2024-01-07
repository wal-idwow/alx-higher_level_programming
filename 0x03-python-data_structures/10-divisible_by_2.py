#!/usr/bin/python3
#find all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    # true if digit / 2 = 0, false if not
    return [True if num % 2 == 0 else False for num in my_list]
