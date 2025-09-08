#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = []
    sum = 0
    for elt in my_list:
        if elt not in seen:
            sum += elt
            seen.append(elt)

    return sum
