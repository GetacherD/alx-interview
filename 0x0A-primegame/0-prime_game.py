#!/usr/bin/python3
"""
prime Number Guess game
apply memoization/caching to avoid repetitive calculation
store all possible prime numbers
    by calculating once here in cache array
"""


def isWinner(x, nums):
    """check who is all round winner"""
    def is_prime(number):
        """ calculate prime numbers"""
        upper = int((number ** 0.5)) + 1
        for factor in range(2, upper):
            if number % factor == 0:
                return False
        return True
    cache = []
    for i in range(2, max(nums) + 1):
        if is_prime(i):
            cache.append(i)
    win_maria = 0
    win_ben = 0
    len_cache = len(cache)
    if x >= len(nums):
        x = len(nums)
    for index in range(x):
        n = nums[index]
        maria = False
        ben = True
        i = 0
        while i < len_cache and cache[i] <= n:
            maria = not maria
            ben = not ben
            i += 1
        if maria:
            win_maria += 1
        if ben:
            win_ben += 1
    if win_ben > win_maria:
        return "Ben"
    if win_maria > win_ben:
        return "Maria"
    return None
