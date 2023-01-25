#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = set(my_list[:])
    unique = 0
    for value in numbers:
        unique += value
    return unique
