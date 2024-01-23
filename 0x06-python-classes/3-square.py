#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class that defines square properties.

    Attributes:
        size: square size
    """
    def __init__(self, size=0):
        """
        Create a new instance of a square.

        Args:
            size (int): Square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: Current square area
        """
        return self.__size ** 2
