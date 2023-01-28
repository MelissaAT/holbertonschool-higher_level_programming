#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divisions = []
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                divisions.append(my_list_1[i] / my_list_2[i])
            else:
                print("wrong type")
                divisions.append(0)
        except ZeroDivisionError:
            print("division by 0")
            divisions.append(0)
        except IndexError:
            print("out of range")
            divisions.append(0)
    return divisions
