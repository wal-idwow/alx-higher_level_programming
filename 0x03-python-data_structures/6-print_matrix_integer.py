#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for smatrix in matrix:
        if len(smatrix) == 0:
            print()
        for i in range(len(smatrix)):
            print("{:d}".format(smatrix[i]),
                end="\n" if i is len(smatrix) - 1 else " ")