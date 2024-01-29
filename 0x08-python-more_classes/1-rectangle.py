#!/usr/bin/python3
"""define a class Rectangle"""


class Rectangle:
    """class Rectangle defines a rectangle by: (based on 0-rectangle.py)
        attribute:
            width (int): rectangle width
            height (int): rectangle height
    """
    def __init__(self, width=0, height=0):
        """new instance of rectangle

        Args:
            width (int): rectangle width. Defaults to 0.
            height (int): rectangle height. Defaults to 0.
        """
        self.height = height
        self.width = width
    
    @property
    def width(self):
        """retrive width
            Returns:
                int: rectangle width
        """
        return self.__height

    @property
    def height(self):
        """retrive height
            Returns:
                int: rectangle height
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """setter of rectangle width
            Args:
                value (int): rectangle width
            Raise:
                TypeError: if width is not an intager.
                ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @height.setter
    def height(self, value):
        """setter of recyangle height.
        Args:
            value (int): rectangle height.
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
