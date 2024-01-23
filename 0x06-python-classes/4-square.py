#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """
    Class that defines square properties.

    Attributes:
        size: square size
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Returns the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
