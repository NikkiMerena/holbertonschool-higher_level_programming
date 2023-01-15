#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for innerList in list(matrix):
        for i, ints in enumerate(list(innerList)):
            if(i != 0):
                print("{}".format(" "), end="")
            print("{:d}".format(ints), end="")
        print()
