#!/usr/bin/python3
"""Task 1 - Divide items in a matrix"""


def bail():
    raise TypeError(
        "matrix must be a matrix (list of lists) of integers/floats")


def matrix_divided(matrix, div):
    """Divide items in matrix by div"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    last = None
    newMatrix = []
    for row in matrix:
        if last is not None and last != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        newMatrix.append(
            [round(x/div, 2) if isinstance(x, (int, float)) else bail()
             for x in row])
        last = len(row)
    return newMatrix
