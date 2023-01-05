#!/usr/bin/python3
"""
LOck Box
"""


def canUnlockAll(boxes):
    """ check if we can unlock all boxes"""
    if (boxes == [[]]):
        return False
    visited = set(boxes[0])
    visited.add(0)
    keys = set(boxes[0])
    tmp = set()
    len_visited = len(visited)
    while True:
        for key in keys:
            for k in boxes[key]:
                tmp.add(k)
                visited.add(k)
        if len(tmp) == 0:
            break
        if (len(visited) == len_visited):
            break
        keys = tmp.copy()
        tmp = set()
        len_visited = len(visited)
    if len(visited) == len(boxes):
        return True
    return False
