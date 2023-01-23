#!/usr/bin/python3
def no_c(my_string):
    characters = my_string.translate({ord(a): None for i in 'cC'})
    return (characters)
