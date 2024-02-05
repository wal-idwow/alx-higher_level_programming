#!usr/bin/python3
"""Module with MyList class"""


class MyList(list):
    """class with method print_sorted"""
    pass

    def print_sorted(self):
        """methde printing list sorted"""
        print(sorted(list(self)))
