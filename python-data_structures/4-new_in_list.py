#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list

    if new_in_list[idx] == idx:
        new_in_list = element
        return new_in_list