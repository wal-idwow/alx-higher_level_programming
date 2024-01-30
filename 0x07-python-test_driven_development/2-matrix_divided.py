#!/usr/bin/python3
"""matrix_divided Module"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (int): elements to be divided by div
        div (int): number dividing

    Raises:
        TypeError: if div is not int or float
        TypeError: if each row of matrix isnot with same size
        TypeError: if matrix is not a list of lists 
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
   