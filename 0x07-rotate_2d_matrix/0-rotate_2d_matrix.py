#!/usr/bin/python3
"""
rotate_2d_matrix in place
"""


def rotate_2d_matrix(matrix):
    """ roatete 2D matrix in place 90 degree"""
    n = len(matrix)
    for k in range(n//2+1):
        count = n - k - k
        reduced = count - 1
        org = matrix[k][k: k + count]
        for i in range(reduced):
            matrix[k][i+k] = matrix[k+reduced - i][k]
        for i in range(reduced):
            matrix[k+1+i][k] = matrix[k+reduced][k+i+1]
        for i in range(reduced - 1):
            matrix[k+reduced][k+1+i] = matrix[k+reduced-1-i][k+reduced]
        for i in range(count):
            matrix[i+k][k+reduced] = org[i]
