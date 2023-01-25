#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for index, item in enumerate(new_list):
        if item == index:
            new_list[index] = index
            return (new_list)
