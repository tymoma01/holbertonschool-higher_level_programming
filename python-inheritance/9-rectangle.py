#!/usr/bin/python3
"""
Documentation
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle empty class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def str(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))