#!/usr/bin/python3
"""
Defines a class Square
"""

class Square:
    """
    define square properties by: (based on 1-square.py)

    Attributes:
        size: square size
    """
    def __init__(self, size=0, position=(0, 0)):
        """creates new instances of square.

        Args:
            size (int): size of the square (1 side).
            position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Returns the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculates the area of square.

        Returns: the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """prints square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
