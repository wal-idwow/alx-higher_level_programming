#!/usr/bin/pyhton3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square and his inherits Rectangle"""


    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str method"""
        first_str = "[Square]"
        second_str = " ({}) ".format(self. id)
        third_str = "{}/{} - ".format(self.x, self.y)
        fourth_str = "{}/{}".format(self.width, self.height)

        return first_str + second_str + third_str + fourth_str

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method update"""
        if args is not None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictioanry with his attributes"""
        attr = ['id', 'x', 'y', 'size']
        prop = {}

        for key in attr:
            if key == 'size':
                prop[key] = getattr(self, 'width')
            else:
                prop[key] = getattr(self, key)

        return prop
