#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
    except IndexError:
        print(IndexError)  # index error will be raised if the index is out of range
        return printed_integers
      
    print ()
    return printed_integers
