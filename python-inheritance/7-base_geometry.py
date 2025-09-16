#!/usr/bin/python3
"""
Documentation
"""

class BaseGeometry:
    """Basegeometry empty class"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validate that value is an integer > 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
        