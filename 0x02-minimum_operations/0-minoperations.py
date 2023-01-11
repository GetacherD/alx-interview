#!/usr/bin/python3
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
        for i in range(2, int(round(n ** 0.5)) + 1, 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, 1 + int(round(n**0.5)), 1):
        if n % i == 0:
            if is_prime(i) or i == 2:
                factors.append(i)
    res = []
    for i in factors:
        res.append(i)
    if res == [] and is_prime(n):
        return n
    if n == 2:
        res.append(2)
    for factor in factors:
        i = 2
        while n % (factor ** i) == 0:
            res.append(factor)
            i += 1
    final = res.copy()
    mul = 1
    for i in res:
        mul *= i
    if (n // mul) != 1:
        final.append(n // mul)
        return sum(final)
    return sum(res)
