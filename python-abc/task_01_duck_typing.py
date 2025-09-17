#!/usr/bin/python3
"""
Documentation
"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Animal class
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):
    """
    Circle class
    """
    def __init__(self, radius):
        if not isinstance(radius, int):
            raise TypeError("Radius should be an int")

        self.__radius = radius

    def area(self):
        return math.pi * self.__radius**2

    def perimeter(self):
        return 2 * math.pi * abs(self.__radius)

class Rectangle(Shape):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError("Width should be an int")
        if not isinstance(height, int):
            raise TypeError("Height should be an int")
        
        self.__width = width
        self.__height = height

    def area(self):
        return abs(self.__width) * abs(self.__height)

    def perimeter(self):
        return abs((self.__width) + (self.__height)) * 2


def shape_info(object):
    print("Area: {}".format(object.area()))
    print("Perimeter: {}".format(object.perimeter()))
