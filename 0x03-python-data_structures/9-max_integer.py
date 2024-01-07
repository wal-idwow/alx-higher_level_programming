#!/usr/bin/python3
#find the biggest integer of a list.
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    list_cp = my_list.copy()
    list_cp.sort()
    return list_cp[-1]
