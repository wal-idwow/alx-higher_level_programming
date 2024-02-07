#!/usr/bin/python3
"""Define pascal trinagle function"""


def pascal_triangle(n):
    """Pascals triangle"""
    lists = []
    triangle = [[1]]

    if n <= 0:
        return lists
    for x in range(1, n):
        row = [1]
        for i in range(1, x):
            row.append(triangle[x-1][i-1] + triangle[x-1][i])
        row.append(1)
        triangle.append(row)

    return triangle
