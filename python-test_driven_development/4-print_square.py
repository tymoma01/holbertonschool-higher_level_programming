#!/usr/bin/python3
"""
here is some documentation
"""

def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    print("\n".join("#" * size for _ in range(size)))
