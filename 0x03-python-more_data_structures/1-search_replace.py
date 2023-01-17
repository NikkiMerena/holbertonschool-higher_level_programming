#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newlist = []
    for x in my_list:
        newlist.append(replace if x == search else x)
    return newlist
