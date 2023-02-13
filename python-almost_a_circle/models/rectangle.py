#!/usr/bin/python3
"""comment Modules"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if width is not int:
           raise TypeError(f"{width} must be an integer")
        else:
            if width < 0:
             raise ValueError(f"{width} must be > 0")
            self.__width = width

        if height is not int:
           raise TypeError(f"{height} must be an integer")
        if height < 0:
           raise ValueError(f"{height} must be > 0")
        self.__height = height

        if x is not int:
           raise TypeError(f"{x} must be an integer")
        elif x < 0:
           raise ValueError(f"{x} must be > 0")
        self.__x = x

        if y is not int:
            TypeError(f"{y} must be an integer")
        elif y < 0:(f"{y} must be > 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            TypeError(f"{value} must be an integer")
        elif value < 0:
            ValueError(f"{value} must be > 0")
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            TypeError(f"{value} must be an integer")
        elif value < 0:
            ValueError(f"{value} must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            TypeError(f"{value} must be an integer")
        elif value < 0:
            ValueError(f"{value} must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            TypeError(f"{value} must be an integer")
        elif value < 0:
            ValueError(f"{value} must be > 0")
        self.__y = value
