#!/usr/bin/python3
"""class and inherited check-class function"""


def is_kind_of_class(obj, a_class):
    """check for object is an instance or inherited instance of a_class

    Args:
        obj (object): object to check
        a_class (class): type of object same as class

    Returns:
        True: if obj is an instance or inherited instance of a_class
        False: if not
    """
    if isinstance(obj, a_class):
        return True
    return False
