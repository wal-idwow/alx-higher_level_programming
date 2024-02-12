#!/usr/bin/python3
"""Rectangle class Module"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle and his inherits Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """x direction of rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y direction of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """y stter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def display(self):
        """prints in stdout the Rectangle"""
        rec = self.y * "\n"
        for n in range(self.height):
            rec += (" " * self.x)
            rec += ("#" * self.width) + "\n"

        print(rec, end='')

    def __str__(self):
        """str method"""
        first_str = "[Rectangle]"
        second_str = " ({}) ".format(self.id)
        third_str = "{}/{} - ".format(self.x, self.y)
        fourth_str = "{}/{}".format(self.width, self.height)

        return first_str + second_str + third_str + fourth_str


    def update(self, *args, **kwargs):
        """update methode"""
        if args is not None and len(args) != 0:
            elem = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, elem[i], args[i])
        else:
            for key, value, in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """returns the area of the square"""
        return self.width * self.height

    def to_dictionary(self):
        """methode to return dictioanry and his properties"""
        attr = ['x', 'y', 'id', 'height', 'width']
        prop = {}

        for key in attr:
            prop[key] = getattr(self, key)

        return prop
        