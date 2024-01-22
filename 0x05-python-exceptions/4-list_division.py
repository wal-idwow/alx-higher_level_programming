#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []

    for i in range(list_length):
        try:
            num_1 = my_list_1[i]
            num_2 = my_list_2[i]

            if not isinstance(num_1, (int, float)) or not isinstance(num_2, (int, float)):
                raise ValueError("wrong type")

            if num_2 == 0:
                raise ZeroDivisionError("division by 0")

            operation = num_1 / num_2
            results.append(operation)

        except IndexError:
            print("out of range")
            results.append(0)

        except (ValueError, ZeroDivisionError) as e:
            print(e)
            results.append(0)

        finally:
            pass

    return results
