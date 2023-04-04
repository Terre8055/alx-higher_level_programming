#!/usr/bin/python3
""" this is my add_integer module """


def add_integer(a, b=98):
    """Returns the addition of a and b.

    Args:
        a: An integer.
        b: An integer. Default value is 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
