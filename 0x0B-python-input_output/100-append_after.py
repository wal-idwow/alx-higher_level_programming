#!/usr/bin/python3
"""define a text file insert function"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file after each line containing specific str"""
    cont = ""
    with open(filename) as i:
        for ln in i:
            cont += ln
            if search_string in ln:
                cont += new_string
    with open(filename, "w") as w:
        w.write(cont)
