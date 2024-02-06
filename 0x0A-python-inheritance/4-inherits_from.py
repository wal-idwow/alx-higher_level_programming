#/usr/bin/python3
"""Define class and inherited check-class function"""


def inherits_from(obj, a_class):
    """check for object is inherited instance of a_class

    Args:
        obj (object): object to check
        a_class (type): type of object same as class

    Returns:
        True: if obj is inherited instance of a_class
        False: if not
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
