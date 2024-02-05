#!/usr/bin/python3
"""
    Method lookup module
"""
def lookup(obj):
    """fonction that return the attributes and methods of an object

    Args:
        obj (object): object for which attributes and methods are to be looked up
    """
    return dir(obj)
