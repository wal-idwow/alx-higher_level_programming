#!/usr/bin/python3
"""define function to add attributes to objects"""


def add_attribute(obj, name, value):
    """Add attribute to object if possible, else raise TypeError.

    Args:
        obj (object): object to add an attr to it
        name (str): name of attr to add to obj
        value (any): value of attr

    Raises:
        TypeError: if the attr can't be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
