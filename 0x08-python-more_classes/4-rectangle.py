#!/usr/bin/python3
""" This module defines a Rectangle class with width, height attributes
    and methods for calculating area, perimeter, printing the rectangle,
    and comparing rectangles.
"""


class Rectangle:
    """ A rectangle class with width, height attributes.

        Attributes:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Class Attributes:
            number_of_instances (int): the number of Rectangle instances
            print_symbol (any): the symbol used for printing the rectangle

        Methods:
            __init__(self, width=0, height=0): initializes the attributes
            area(self): calculates the area of the rectangle
            perimeter(self): calculates the perimeter of the rectangle
            __str__(self): returns the string representation of the rectangle
            __repr__(self): returns the string representation of the rectangle
            __del__(self): prints a message when an instance is deleted
            bigger_or_equal(rect_1, rect_2): returns the biggest rectangle
            square(cls, size=0): returns a square Rectangle instance
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance with width and height values.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Retrieves the value of the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of the width attribute.

        Args:
            value (int): the value to set as width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves the value of the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of the height attribute.

        Args:
            value (int): the value to set as height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of the rectangle.

        Returns:
            The area of the rectangle (int).
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle (int).
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width) * 2 + (self.__height * 2)

    def __str__(self):
        """ Returns the string representation of the rectangle. """
        string = ""
        if self.__width is 0 or self.__height is 0:

