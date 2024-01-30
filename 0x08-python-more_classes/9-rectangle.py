#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Class Rectangle with validated private instance attributes width and height

    Attributes:
        number_of_instances: number of instances of Rectangle
        print_symbol: symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int):  width of  new rectangle.
            height (int):  height of  new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height.

        Args:
            value (int):  height of  rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get the widht of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width.

        Args:
            value (int):  width of  rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """returns  calculated area of Rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """returns  calculated perimeter of Rectangle instance"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string of Rectangle instance using #, empty string"""
        str_list = []
        for x in range(self.__height):
            for j in range(self.__width):
                str_list.append("{0}".format(self.print_symbol))
            if x is not (self.__height - 1):
                str_list.append('\n')
        return ''.join(str_list)

    def __repr__(self):
        """returns a string representation able to create new instance"""
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        """prints 'Bye rectangle...' when instance is deleted"""
        print ("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns  bigger Rectangle or rect_1 if they are equal

        Raises:
            TypeError: if rect_1 is not a Rectangle
            TypeError: if rect_2 is not a Rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
