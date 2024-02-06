#!usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """class with method print_sorted"""
    pass

    def print_sorted(self):
        """methde printing list sorted"""
        print(sorted(list(self)))
