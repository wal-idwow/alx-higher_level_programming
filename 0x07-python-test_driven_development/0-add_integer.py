#!/usr/bin/python3
"""
 add_integer methode Module
"""
def add_integer(a, b=98):
    """Adds two integers : (a)(b)
    Returns: int: result (a + b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    #converts a and b to int
    a = int(a)
    b = int(b)

    return a + b
