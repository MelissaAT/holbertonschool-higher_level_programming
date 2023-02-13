#!/usr/bin/python3
"""Comment Module"""


class Base:
    """comment class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.__id = id
    
        else:
            Base.__nb_objects = self.__id
