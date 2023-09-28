#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of intergers representing pascal triangle
    returns empty list when n is zero
    """
    if n <= 0:
        return []
    pascal = []
    for row in range(1, n + 1):
        new_row = []
        for post in range(row):
            if post == row - 1:
                new_row.append(1)
            elif post == 0:
                new_row.append(1)
            else:
                try:
                    new_row.append(pascal[row - 2][post - 1] +
                                   pascal[row - 2][post])
                except IndexError:
                    pass
        pascal.append(new_row)
    return pascal
