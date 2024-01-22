#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_nb = 0

    try:
        for index in range(x):
            print("{}".format(my_list[index]), end="")
            real_nb += 1
    except IndexError:
        pass
    print()
    return real_nb
