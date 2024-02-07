#!/usr/bin/python3
"""define a function to append a file"""


def append_write(filename="", text=""):
    """append str in the end of a UTF8 file.txt

    Args:
        filename (str): file name. Defaults to "".
        text (str): string to append. Defaults to "".
    
    Returns:
        number of character appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
