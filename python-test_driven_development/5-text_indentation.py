#!/usr/bin/python3
"""
This module imports a function that
reformats a string of by adding newlines
after specific characters are identified
"""


def text_indentation(text):
    """
    Function that prints a text with two
    newlines after each '.', '?' and ':'
        Args:
            text (str): string of text to print
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    empty = True
    for spaces in text:
        if spaces != " ":
            empty = False
    
    if empty == False:
        if text != "" and text[0] == " ":
            text = text[1:]
        if text != "" and text[len(text) - 1] == " ":
            text = text[:len(text) - 1]
        last_char = " "
        for char in text:
            if char == '.' or char == '?' or char == ':':
                print(char)
                print()
                last_char = char
            else:
                if last_char == '.' or last_char == '?' or last_char == ':':
                    last_char = " "
                    continue
                print(char, end="")
