#!/usr/bin/python3
"""Define a student by Fs/Ls name, age"""
class Student:
    """Student Class"""


    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation"""
        if (isinstance(attrs, list) and
                all(isinstance(i, str) for i in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
