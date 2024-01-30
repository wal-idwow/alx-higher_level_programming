#!/usr/bin/python3
"""
print_square Module 
Prints a square with the character #.
"""


def print_square(size):
    """prints square where size is
    length and width of square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
