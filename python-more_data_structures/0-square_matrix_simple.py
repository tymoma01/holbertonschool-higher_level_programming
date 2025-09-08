#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in range(len(matrix)):
        line = []
        for j in range(len(matrix[0])):
            line.append(matrix[i][j]**2)
        res.append(line)

    return res
