#!/usr/bin/python3
""" My class module
"""

class Student:
    """ My class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr : self.__dict__[attr] 
                    for attr in attrs 
                    if attr in self.__dict__.keys()}
        return self.__dict__