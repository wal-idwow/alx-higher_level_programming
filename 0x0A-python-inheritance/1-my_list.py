#!usr/bin/python3
"""Method with Mylist class"""


class Mylist(list):
    """class with method print_sorted"""
    pass

    def print_sorted(self):
        """methde to sorted list"""
        print(sorted(list(self)))
