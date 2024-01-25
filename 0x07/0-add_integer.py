#!/usr/bin/python3
""" Module for add_integer methode """


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a : first number
        b : second number. Defaults to 98.

    Returns:
        int: result of (a + b)

    Raises:
        TypeError: If a or b is not an integr or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    #cast 'a' and 'b' to int if thay are floats
    a = int(a)
    b = int(b)

    return a + b
