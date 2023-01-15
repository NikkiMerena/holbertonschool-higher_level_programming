#!/usr/bin/python3

def no_c(my_str):
    _list = [char for char in my_str if char != 'c']
    _list = [char for char in _list if char != 'C']
    my_str = "".join(_list)
    return my_str
