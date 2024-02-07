#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """invert int operators == and !=."""

    def is_equal(self, value):
        """override == operator with != behavior."""
        return super().__ne__(value)

    def is_not_equal(self, value):
        """override != operator with == behavior."""
        return super().__eq__(value)
