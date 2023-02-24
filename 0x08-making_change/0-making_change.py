#!/usr/bin/python3
"""
Make changes
"""


stack = []


def solve(ls, total, i):
    """ helper solve function """
    global stack
    if total == 0:
        return
    if i >= len(ls):
        stack = []
        return
    if total > 0:
        stack.append(ls[i])
        total -= ls[i]
        solve(ls, total, i)
    elif total < 0:
        stack.pop()
        total += ls[i]
        i += 1
        solve(ls, total, i)


def makeChange(coins, total):
    """ make changes """
    global stack
    if total <= 0:
        return 0
    coins = sorted(list(set(coins)), reverse=True)
    solve(coins, total, 0)
    if stack == []:
        return -1
    return len(stack)
