#!/usr/bin/python3
"""comment Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for the size of the sqaure"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the square object"""
        return (f'[Square] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}')
