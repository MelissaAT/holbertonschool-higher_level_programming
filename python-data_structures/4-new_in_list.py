#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    for i in range(len(my_list)):
        if new_in_list[i] == idx:
            new_in_list = element
            return new_in_list