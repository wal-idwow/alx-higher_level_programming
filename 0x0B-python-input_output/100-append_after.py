#!/usr/bin/python3
"""Define a text file insert function"""


def append_after(filename="", search_string="", new_string=""):
    """ function inserts line of text to a file"""
    cont = ""
    with open(filename) as i:
        for ln in i:
            cont += ln
            if search_string in ln:
                cont += new_string
    with open(filename, "w") as w:
        w.write(cont)
