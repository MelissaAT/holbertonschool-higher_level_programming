#!/usr/bin/python3
"""comment"""


class MyInt(int):
    """comment"""
    def __eq__(self, other):
        return int(self) != int(other)
    
    def __ne__(self, other):
        return int(self) == int(other)
