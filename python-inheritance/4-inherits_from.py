#!/usr/bin/python3
"""
Documentation
"""

def inherits_from(obj, a_class):
    """Check if obj is kind class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    # return isinstance(obj, a_class) and not type(obj) is a_class
    