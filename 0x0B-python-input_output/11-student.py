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
        if attrs is None or not all(isinstance(i, str) for i in attrs):
            return self.__dict__.copy()

        return {i: getattr(self, i, None) for i in attrs}

    def reload_from_json(self, json):
        """change attr of student inst"""
        for key, value in json.items():
            setattr(self, key, value)
