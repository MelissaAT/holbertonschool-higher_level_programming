#!/usr/bin/python3
"""
write a function that reads a text file 
(UFT8) and prints it to stdout
"""


def read_file(filename=""):
    with open(filename="") as f:
        lines = f.readlines()