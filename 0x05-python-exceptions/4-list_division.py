#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    results = []
    i = 0
    num_1 = my_list_1[i]
    num_2 = my_list_2[i]
    
    for i in range(list_length):
        try:
            operation = num_1 / num_2
        except ZeroDivisionError:
            print("division by 0")
            operation = 0
        except TypeError:
            print("wrong type")
            operation = 0
        except IndexError:
            print("out of range")
            operation = 0
        finally:
            results.append(operation)
    return operation
