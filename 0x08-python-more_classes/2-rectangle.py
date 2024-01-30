#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """Class that defines properties of a rectangle.

    Attributes:
        length (int): Length of the rectangle.
        height (int):height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates a new instance of Rectangle
        
        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width.

        Returns:
            int: The length of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the length.

        Args:
            value (int): The length of the rectangle.

        Raises:
            TypeError: If length is not an integer.
            ValueError: If length is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height.

        Args:
            value (int): the rectangle height.

        Raises:
            TypeError: Ifheight is not an integer.
            ValueError: Ifheight is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter.
        """
        return 0 if self.__width == 0 or self.__height == 0 else 2 * (self.__width + self.__height)
