#!/usr/bin/python3
"""
here is some documentation
"""

def text_indentation(text) :

    "Here is some more documentation"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buffer = ""
    for ch in text:
        buffer += ch
        if ch in ".?:":
            print(buffer.strip(), end="")
            print("\n")
            buffer = ""

    if buffer.strip():
        print(buffer.strip(), end="")
