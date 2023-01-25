#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for replace, search in enumerate(my_list):
        if search == 2:
            my_list[replace] = 89
    return(my_list)
