#!/usr/bin/python3
#removes all characters c and C from a string.
def no_c(my_string):
    fn = ""
    for num in range(len(my_string)):
        if (my_string[num] != 'C' and my_string[num] != 'c'):
            fn += my_string[num]
    return fn 
        