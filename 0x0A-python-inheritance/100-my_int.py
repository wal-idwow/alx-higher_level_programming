#!/usr/bin/python3
"""defines a class MyInt that inherits from int."""

class MyInt(int):
    """invert int operators == and !=."""

    def __new__(cls, value):
        """create new instance with inverted behavior."""
        return super().__new__(cls, value)

    def __eq__(self, value):
        """override == opeartor with != behavior."""
        return super().__ne__(value)

    def __ne__(self, value):
        """override != operator with == behavior."""
        return super().__eq__(value)
