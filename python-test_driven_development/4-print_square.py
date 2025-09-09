#!/usr/bin/python3
"""
here is some documentation
"""

def print_square(size):
    "Here is some more documentation"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
