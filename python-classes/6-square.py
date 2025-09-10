#!/usr/bin/python3
"""
Here is some documentation
"""
class Square:
    """
    Here is some more documentation
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple[0]) or not isinstance(value, tuple[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end='')
            print("#" * self.size)

    