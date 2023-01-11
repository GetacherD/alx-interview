#!/usr/bin/env python3
"""
Minimum Operations
"""


def minOperations(n):
    """ Min operations"""
    if n <= 1:
        return 0
    factors = []

    def is_prime(n):
        if n == 2:
            return True
        for i in range(2, n // 2 + 1, 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, 1 + n // 2, 1):
        if n % i == 0:
            if is_prime(i) or i == 2:
                factors.append(i)
    res = factors.copy()
    if res == [] and is_prime(n):
        return n
    if n == 2:
        res.append(2)
    for factor in factors:
        i = 2
        while n % (factor ** i) == 0:
            res.append(factor)
            i += 1
    return sum(res)
