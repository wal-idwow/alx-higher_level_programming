#!/usr/bin/python3
"""
say_my_name Module
Prints first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with the provided first name and last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
