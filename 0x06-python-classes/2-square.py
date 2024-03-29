#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    define square properties by: (based on 1-square.py)

    Attributes:
        size: square size
    """
    def __init__(self, size=0):
        """new instance of square

        Args:
            size: square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
