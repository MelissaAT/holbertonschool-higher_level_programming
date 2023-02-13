#!/usr/bin/python3
"""comment Modules"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if width is not int:
           raise TypeError("width must be an integer")
        else:
            if width < 0:
             raise ValueError("width must be > 0")
            self.__width = width

        if height is not int:
           raise TypeError("height must be an integer")
        if height < 0:
           raise ValueError("height must be > 0")
        self.__height = height

        if x is not int:
           raise TypeError("x must be an integer")
        elif x < 0:
           raise ValueError("x must be > 0")
        self.__x = x

        if y is not int:
            TypeError("y must be an integer")
        elif y < 0:("y must be > 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            TypeError("width must be an integer")
        elif value < 0:
            ValueError("width must be > 0")
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            TypeError("height must be an integer")
        elif value < 0:
            ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            TypeError("x must be an integer")
        elif value < 0:
            ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            TypeError("y must be an integer")
        elif value < 0:
            ValueError("y must be > 0")
        self.__y = value
