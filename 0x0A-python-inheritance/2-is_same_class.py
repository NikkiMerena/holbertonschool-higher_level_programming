#!/usr/bin/python3
"""
Exact same object- returns True if the same, otherwise Fals
"""

def is_same_class(obj, a_class):
    """
    Checks if obj1 and obj2 are the exact same instance
    """
    if type(obj) == a_class:
        return True
    else:
        return False
