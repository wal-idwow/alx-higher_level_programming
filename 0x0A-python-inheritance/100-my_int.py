#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """invert int operators == and !=."""

    def is_equal(self, other):
        """override == operator with != behavior."""
        return super().__ne__(other)

    def is_not(self, other):
        """override != operator with == behavior."""
        return super().__eq__(other)
