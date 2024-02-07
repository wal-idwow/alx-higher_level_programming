#!/usr/bin/python3
"""define a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """print the content of a UTF8 text file to stdout

    Args:
        filename (file): name of the file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
