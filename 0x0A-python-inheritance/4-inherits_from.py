#!/usr/bin/python3
"""Define class and inherited check-class function"""


def inherits_from(obj, a_class):
    """Check if object is an instance inherited from a_class

    Args:
        obj (object): Object to check
        a_class (type): Type of object, representing a class

    Returns:
        True if obj is an instance inherited from a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
