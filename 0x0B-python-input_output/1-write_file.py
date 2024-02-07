#!/usr/bin/python3
"""define function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str): file name. Defaults to "".
        text (str): text written in the file. Defaults to "".

    Returns:
        Number of character written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
