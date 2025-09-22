#!/usr/bin/python3
"""
Here is some documentation
"""
def read_file(filename=""):
    with open(filename) as f:
        print(f.read())