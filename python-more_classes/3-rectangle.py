#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """Class Rectangle defines width and height and raise exeptions
    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        _area = self.__width * self.__height
        return _area

    def perimeter(self):
        if self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        rectangle_print = ""
        for i in range(self.__height):
            if i != 0:
                rectangle_print += "\n"
            for j in range(self.__width):
                rectangle_print += "#"
        return rectangle_print
