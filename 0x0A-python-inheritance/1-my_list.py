#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """Method for printing the sorted list"""
        self.sort()
        print(self)
