#!/usr/bin/python3
"""Define a function to append a file"""


def append_write(filename="", text=""):
    """function to append str in the end of a UTF8 file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
