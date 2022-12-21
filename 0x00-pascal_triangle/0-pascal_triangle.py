#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """Generate Pascal Triangle"""
    prev = []
    if (n <= 0):
        yield []
    yield [1]
    for i in range(n - 1):
        next = [1]
        for j in range(len(prev) - 1):
            next.append(prev[j] + prev[j + 1])
        next.append(1)
        prev = next
        yield next
