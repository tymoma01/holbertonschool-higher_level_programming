#!/usr/bin/python3
"""
Documentation
"""

class MyList(list):
    """
    class that inherits from list
    """

    def print_sorted(self):
        print(sorted(self))