#!/usr/bin/python3
#prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for smatrix in matrix:
        if len(smatrix) == 0:
            print()
        for num in range(len(smatrix)):
            print("{:d}".format(smatrix[num]),
                end="\n" if num is len(smatrix) - 1 else " ")
       