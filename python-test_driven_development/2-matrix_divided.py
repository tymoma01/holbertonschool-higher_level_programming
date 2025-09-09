#!/usr/bin/python3
"""
matrix_divided(matrix, div) -> new_matrix

Divides all elements of a matrix by a number and returns a new matrix whose
elements are rounded to 2 decimal places.

Rules:
- `matrix` must be a list of lists of integers/floats,
  otherwise raise: TypeError("matrix must be a matrix (list of lists) of integers/floats")
- All rows must have the same size,
  otherwise raise: TypeError("Each row of the matrix must have the same size")
- `div` must be an int or float,
  otherwise raise: TypeError("div must be a number")
- `div` cannot be 0,
  otherwise raise: ZeroDivisionError("division by zero")
"""

def matrix_divided(matrix, div):
    """Divide all elements of `matrix` by `div` and round to 2 decimals."""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_len = None
    for row in matrix:
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elt in row:
            if not isinstance(elt, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(elt / div, 2) for elt in row] for row in matrix]