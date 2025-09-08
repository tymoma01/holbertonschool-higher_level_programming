#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for elt in my_list[::-1]:
        print("{:d}".format(elt))