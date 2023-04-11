#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Represents an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the behavior of the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """Invert the behavior of the != operator."""
        return int(self) == other
