#!/usr/bin/python3
"""
Documentation
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Animal class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class
    """

    def sound(self):
        return "Bark"
    
class Cat(Animal):
    """
    Cat class
    """

    def sound(self):
        return "Meow"