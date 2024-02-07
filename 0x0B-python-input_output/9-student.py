#!/usr/bin/python3
"""Define a student by Fs/Ls name, age"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation"""
        return self.__dict__.copy()
