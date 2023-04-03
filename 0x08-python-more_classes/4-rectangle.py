#!/usr/bin/python3
"""
Module that defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle Class
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle
        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle
        Args:
            value (int): Width of the rectangle
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle
        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle
        Args:
            value (int): Height of the rectangle
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the '#' char
        Returns:
            String representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += "#"
            rect += "\n"
        rect = rect[:-1]
        return rect

    def __repr__(self):
        """
        Returns a string representation of the rectangle instance
        Returns:
            String representation of the rectangle instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)
