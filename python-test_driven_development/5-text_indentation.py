#!/usr/bin/python3
"""
here is some documentation
"""

def text_indentation(text):
    "Here is some more documentation"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ":.?":
        text = text.replace(delim, delim + '\n\n')
    
    for line in text.split('\n'):
        line = line.strip()
       
        print(line)