#!/usr/bin/python3
"""
Here is some documentation
"""
def read_file(filename=""):
    """Here is some more documentation"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")