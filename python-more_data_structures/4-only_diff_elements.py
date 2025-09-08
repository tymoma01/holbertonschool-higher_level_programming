#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = []
    for elt1 in set_1:
        if elt1 not in set_2:
            res.append(elt1)
    for elt2 in set_2:
        if elt2 not in set_1 and elt2 not in res:
            res.append(elt2)
    return res