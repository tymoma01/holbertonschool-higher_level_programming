#!/usr/bin/python3
"""
Here is some documentation
"""
def append_write(filename="", text=""):
    """Here is some more documentation"""
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
