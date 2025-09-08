#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for elt in my_list:
        if isinstance(elt, int):
            print(elt)
    