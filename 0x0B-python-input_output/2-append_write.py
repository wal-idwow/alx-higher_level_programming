#!/usr/bin/python3
"""define a function to append a file"""


def append_write(filename="", text=""):
    """function to append str in the end of a UTF8 file

    Args:
        filename (str): file name.
        text (str): string to append.
    
    Returns:
        number of character appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
