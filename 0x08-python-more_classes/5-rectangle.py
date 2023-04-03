#!/usr/bin/python3
"""
Module - Rectangle
"""


class Rectangle:
    """
    Class that defines a rectangle with properties width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initialization method that sets the values for width and height
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        Returns:
            The value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        Args:
            value (int): The value to be set
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        Returns:
            The value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
        Args:
            value (int): The value to be set
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints the rectangle using '#'
        Returns:
            A string that represents the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """
        Returns:
            A string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints the message 'Bye rectangle...' when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")

