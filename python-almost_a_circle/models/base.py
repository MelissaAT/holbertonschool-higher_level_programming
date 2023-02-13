#!/usr/bin/python3
"""Comment Module"""


class Base:
    """This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your 
    future classes and to avoid duplicating the same code"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.__id = id
        else:
            
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
