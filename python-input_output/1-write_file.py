#!/usr/bin/python3
"""
Here is some documentation
"""
def write_file(filename="", text=""):
    """Here is some more documentation"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
