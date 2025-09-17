#!/usr/bin/python3
"""
Documentation
"""
class MyInt(int):
    """MyInt empty class"""
    def __eq__(self, other):
        return not super().__eq__(other)
    
    def __ne__(self, other):
        return not super().__ne__(other)