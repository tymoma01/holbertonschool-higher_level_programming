#!/usr/bin/python3
""" My class module
"""

def pascal_triangle(n):
    """Pascal triangle function"""
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
        print(f"i: {i}")
        
        row = [1] * (i + 1)
        print(f"row: {row}")

        prev = res[i - 1]
        print(f"prev: {prev}")

        j = 1
        while j < i:
            print(f"j: {j}")

            row[j] = prev[j - 1] + prev[j]
            print(prev[j - 1])
            print(prev[j])
            print(f"row: {row[j]}")
            j += 1
            
        res.append(row)
        print(f"res: {res}")
        i += 1
       
    return res