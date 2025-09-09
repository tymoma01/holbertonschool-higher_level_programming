#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(args)
    except Exception as e:
        print("Exception: {e}".format(e))
        return None