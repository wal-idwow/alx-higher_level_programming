#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  
    results = []
    i = 0

    for i in range(list_length):
        try:
            operation = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            operation = 0
        except ZeroDivisionError:
            print("division by 0")
            operation = 0
        except IndexError:
            print("out of range")
            operation = 0
        finally:
            results.append(operation)
    return results
