#!/usr/bin/python3
""" Write a class that defines a square
"""


class Square:
    """ class square has to be an int
    area(self) returns the current square area 
    """


    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        _area = self.__size * self.__size
        return _area
