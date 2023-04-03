#!/usr/bin/python3
""" Module that defines a Rectangle class """


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width attribute with error handling """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height attribute with error handling """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns the string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """ Returns the formal string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)


