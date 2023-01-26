#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_a = list(a_dictionary.keys())
    key_a.sort()
    for key in key_a:
        print(f"{key}: {a_dictionary.get(key)}")
