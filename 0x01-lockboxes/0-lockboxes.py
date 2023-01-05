#!/usr/bin/python3
"""
LOck Box
"""


def canUnlockAll(boxes):
    """ check if we can unlock all boxes"""
    size = len(boxes)
    visited = set()
    for i in boxes[0]:
        if i < size:
            visited.add(i)
    visited.add(0)
    keys = set(boxes[0])
    tmp = set()
    len_visited = len(visited)
    while True:
        for key in keys:
            if (key >= size):
                continue
            print("used key", key)
            for k in boxes[key]:
                if (k < size):
                    tmp.add(k)
                    visited.add(k)
        if len(tmp) == 0:
            break
        if (len(visited) == len_visited):
            break
        keys = tmp.copy()
        tmp = set()
        len_visited = len(visited)
    print(visited)
    print(boxes)
    if len(visited) == len(boxes):
        return True
    return False
