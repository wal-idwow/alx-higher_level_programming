#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_nb = 0
    
    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            real_nb += 1
    except IndexError:
        pass  # exception raised if index is out of range
    
    print()  # new line after printing all elements
    return real_nb
