#!/usr/bin/python3
def element_at(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
    my_list[idx] = element
    return my_list
    