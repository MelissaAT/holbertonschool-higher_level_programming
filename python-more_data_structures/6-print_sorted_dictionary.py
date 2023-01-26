#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_a = a_dictionary
    sorted_key = dict(sorted(dic_a.items()))
    for key, value in dic_a.items():
        print(f"{key, value}")
