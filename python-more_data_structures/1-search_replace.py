#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for elt in my_list:
        if elt == search:
            res.append(replace)
        else:
            res.append(elt)
    return res