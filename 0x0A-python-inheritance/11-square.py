#!/usr/bin/python3
"""Defines a Rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits srom Rectangle."""

    def __init__(self, size):
        """Initialize a new Square instance
        Args:
            size (int): Size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
