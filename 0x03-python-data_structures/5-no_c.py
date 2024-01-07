#!/usr/bin/python3
def no_c(my_string):
    fn = ""
    for char in my_string:
        if char.lower() != 'c':
            fn += char
    return fn