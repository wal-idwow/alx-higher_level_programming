#!/usr/bin/python3
"""Defines Rectangle class, inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int):  height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return print() and str() representation of a Rectangle."""
        res = "[" + str(self.__class__.__name__) + "] "
        res += str(self.__width) + "/" + str(self.__height)
        return res

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height
