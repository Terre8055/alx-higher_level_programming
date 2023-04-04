#!/usr/bin/python3
""" module that divides all elements of a matrix of similar sized rows """


def matrix_divided(matrix, div):
    """ function that returns a new matrix with each element divided by da div

    Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error

    Returns: a new matrix with each element adjusted to the div amount
    """

    # Check matrix validity
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix and round to 2 decimal places
    return [[round(elem/div, 2) for elem in row] for row in matrix]
