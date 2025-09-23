#!/usr/bin/python3
""" My class module
"""

def pascal_triangle(n):
    res = []
    
    for i in range(1, n + 1):
        row = []
        C = 1
        for j in range(1, i + 1):
            row.append(C)
            C = C * (i - j) // j
        res.append(row)

    return res

def pascal_triangle_1(n):
    if n <= 0:
        return []

    res = [[1]]
    i = 1
    while i < n:
        row = [1] * (i + 1)
        prev = res[i - 1]
        j = 1
        while j < i:
            row[j] = prev[j - 1] + prev[j]
            j += 1
        res.append(row)
        i += 1
    return res