#!/usr/bin/python3
"""This program divides every value in a matrix by a given divisor
"""


def matrix_divided(matrix, div):
    """matrix is the provided matrix, div is the divisor
    The matrix should consist only of ints or floats
    The divisor should also be an int or float, and not zero
    Resultant matrix should have values rounded to two places
    New matrix should be returned
    Each row of the matrix should be the same size
    """

    """Check that divisor is not zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Chech that divisor is present"""
    if div is None:
        raise TypeError("matrix_divided() missing 1\
                        required positional argument: 'div'")

    """Check that divisor is a number"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    """Check that each row of the matrix is the same size"""
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    """Check that each value in the matrix is a number"""
    for row in matrix:
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    """Finally, return a new matrix"""
    return[[round(num/div, 2) for num in row] for row in matrix]
