#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def is_equal(self, other):
        """Override == operator with != behavior."""
        return super().__ne__(other)

    def is_not(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
