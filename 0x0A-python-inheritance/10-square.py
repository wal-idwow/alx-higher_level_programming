#!/usr/bin/python3
"""Define subclass square from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define square class with his inheritance Rectangle"""

    def __init__(self, size):
        """initialize new square

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
