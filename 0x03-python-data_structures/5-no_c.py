#!/usr/bin/python3
def no_c(my_string):
    fn = ""
    for num in range(len(my_string)):
        if (my_string[num] != 'C' and my_string[num] != 'c'):
            fn += my_string[num]
    return (fn)