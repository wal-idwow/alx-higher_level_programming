#!usr/bin/python3
"""Method with Mylist class"""


class MyList(list):
    """class with method print_sorted"""

    def print_sorted(self):
        """methde to print sorted list"""
        print(sorted(list(self)))
