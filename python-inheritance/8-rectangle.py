#!/usr/bin/python3
"""
Write a class BaseGeometry
(based on 6-base_geometry.py).
"""


Rectangle = __import__('8-rectangle').Rectangle

class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
