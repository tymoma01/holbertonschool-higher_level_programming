#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    res = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > best:
                res = k
                best = v
        return res
    return None