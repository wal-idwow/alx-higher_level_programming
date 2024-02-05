#!usr/bin/python3
"""Method with MyList class"""


class MyList(list):
    """class with method print_sorted"""
    pass

    def print_sorted(self):
        """methde printing list sorted"""
        print(sorted(list(self)))
