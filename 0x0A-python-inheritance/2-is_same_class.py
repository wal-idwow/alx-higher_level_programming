#!/usr/bin/python3
"""Module with method is_same_class"""


def is_same_class(obj, a_class):
    """"Method returns True if an object is instance"""

    return type(obj) is a_class
