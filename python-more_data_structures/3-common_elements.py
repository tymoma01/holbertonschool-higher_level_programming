#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = []
    for elt1 in set_1:
        if elt1 in set_2:
            res.append(elt1)
    return res