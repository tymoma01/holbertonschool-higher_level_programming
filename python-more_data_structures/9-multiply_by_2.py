#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    for k, v in a_dictionary.items():
        res[k] = v * 2
    return res